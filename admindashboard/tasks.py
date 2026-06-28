


from matches.models import Match 
from accounts.models import User
from predictions.models import Prediction
from django.db.models import Sum 
from leaderboard.models import Leaderboard

def calculate_match_points(match_id):
    
    try:
        match = Match.objects.get(id=match_id)
    except Match.DoesNotExist:
        return False  , "Match not found"

    if match.home_score is None or match.away_score is None:
        return  False  ,"Match score is incomplete"
    
    actual_home = match.home_score
    actual_away = match.away_score
    
    predictions = Prediction.objects.filter(match = match)
    # users = User.objects.filter()
    
    if actual_home > actual_away:
        actual_result = "HOME"
    elif actual_home < actual_away :
        actual_result ="AWAY"
    else: 
        actual_result ="DRAW"
    
    updated_predictions =[]
    affected_user_ids  = set()
    
    for p in predictions:
        
        predicted_home = p.home_prediction
        predicted_away = p.away_prediction
        
        if(
            predicted_home == actual_home and
            predicted_away==actual_away
        ):
            p.points = 5
            
        else:
            if predicted_home > predicted_away:
                predicted_result = "HOME"
            elif predicted_home < predicted_away:
                predicted_result = "AWAY"
            else:
                predicted_result="DRAW"
                
            
            if predicted_result == actual_result:
                p.points = 3
            else :
                p.points =0
            
        p.is_calculated = True
                
        updated_predictions.append(p)
        affected_user_ids.add(p.user_id)
        
        
        
    Prediction.objects.bulk_update(
        updated_predictions,
        ["points","is_calculated"]
    )           
            
    
    users =User.objects.filter(
        id__in = affected_user_ids
    )
    
    totals = (
        Prediction.objects.filter(
            user_id__in = affected_user_ids
        ).values("user_id")
        .annotate(total=Sum("points"))
    )
    
    total_map ={
        item["user_id"]:item["total"]
        for item in totals
    }
    
    updated_users =[]
    
    for user in users:
        user.total_points=total_map.get(user.id,0)
        updated_users.append(user)
    
    User.objects.bulk_update(
        updated_users,
        ["total_points"]
    )
    
    tournament = match.tournament
    
    leaderboard_updates = []
    
    for user_id in affected_user_ids:
        
        club_ids = Prediction.objects.filter(
            user_id = user_id,
            match__tournament = tournament
        ).values_list("club_id",flat=True).distinct()
        
        for club_id in club_ids:
            total =(
                Prediction.objects.filter(
                    user_id=user_id,
                    club_id=club_id,
                    match__tournament=tournament
                ).aggregate(
                    total=Sum("points")
                )["total"] or 0
            )
            
            leaderboard,_ = Leaderboard.objects.get_or_create(
                user_id = user_id,
                club_id=club_id,
                tournament=tournament
            )
            
            leaderboard.total_points = total
            leaderboard_updates.append(leaderboard)
    Leaderboard.objects.bulk_update(
        leaderboard_updates,
        ["total_points"]
    )
    
    
    return True,"points calculated successfully "
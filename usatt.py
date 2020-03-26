def diff_to_change(diff):
  if diff > 237:
    return 50
  elif diff > 212:
    return 45
  elif diff > 187:
    return 40
  elif diff > 162:
    return 35
  elif diff > 137:
    return 30
  elif diff > 112:
    return 25
  elif diff > 87:
    return 20
  elif diff > 62:
    return 16
  elif diff > 36:
    return 13
  elif diff > 12:
    return 10
  elif diff > -13:
    return 8
  elif diff > -38:
    return 7
  elif diff > -63:
    return 6
  elif diff > -88:
    return 5
  elif diff > -113:
    return 4
  elif diff > -138:
    return 3
  elif diff > -163:
    return 2
  elif diff > -188:
    return 2
  elif diff > -213:
    return 1
  elif diff > -238:
    return 1
  else:
    return 0

def calc_rating(rating, wins, losses):
  final = rating
  for win in wins:
    final += diff_to_change(win - rating)
  for loss in losses:
    final -= diff_to_change(rating - loss)
  return final

def adjustment(rating, wins, losses):
  final = calc_rating(rating, wins, losses)
  if final - rating < 50:
    return rating
  elif final - rating < 75:
    return final
  else:
    best_win = max(wins)
    worst_loss = min(losses)
    avg = (best_win + worst_loss)/2
    if avg > final:
      return (avg + final)/2
    else:
      return final
#print(calc_rating(1800, [1525,1900,1790,1600], [2000,2100,1850]))
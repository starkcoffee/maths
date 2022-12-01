
function experiment(trials)
  tally_wins_if_stay, tally_wins_if_switch = 0,0

  for i in 1:trials
    ghost_behind_door = rand(1:3)
    door_chosen = rand(1:3)

    win_if_stay = ghost_behind_door == door_chosen

    if win_if_stay
      tally_wins_if_stay += 1
    else
      # if the ghost is not behind the door we chose, then it must
      # be behind the only other closed door, so we would win if we switch
      # ie., P(win_if_switch) = 1 - P(win_if_stay)
      tally_wins_if_switch +=1
    end
  end
  (tally_wins_if_stay, tally_wins_if_switch)
 end

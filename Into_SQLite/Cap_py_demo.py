# for Capped_NE_electoral_college

population_per_vote = DF2008.State_Vote_Total" / "column_Num_Reps_Capped"
Intial_votes = column_Candidate_Votes / population_per_vote














Remander_pop = column_Candidate_Votes % population_per_vote
State_remander_pop = 0
for var in state_list:
    if State == var:
        State_remander_pop += Remander_pop
if Remander_pop >= population_per_vote:
    Remander_vote = Remander_pop / population_per_vote
else:
    Remander_vote = 0
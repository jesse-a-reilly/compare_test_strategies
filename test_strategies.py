"""
test_strategies.py
Compares scores obtained on a multiple choice test using two strategies.
Strategy one is choosing an answer at random for each question
Strategy two is choosing C for each answer
In theory, both strategies should yield the same result, on average
"""
import random

# Simulation parameters
QUESTIONS_PER_TEST = 100
ANSWER_OPTIONS = 4
SIMULATION_RUNS = 1000
NON_RANDOM_ANSWER = 2

# store the test results
non_random_answer_scores_array = []
random_answer_scores_array = []

# Run the simulation
for run_no in range(SIMULATION_RUNS):

    # Generate a new test for each run
    test_answers = []
    for x in range(QUESTIONS_PER_TEST):
        test_answers.append(random.randrange(ANSWER_OPTIONS))

    # Take the test using the non-random anwer (i.e. pick C for each question)
    non_random_score = 0
    for x in test_answers:
        if x == NON_RANDOM_ANSWER:
            non_random_score += 1
    non_random_answer_scores_array.append(non_random_score)

    # Take the test using random answers for each question
    random_score = 0
    for x in test_answers:
        if x == random.randrange(ANSWER_OPTIONS):
            random_score += 1
    random_answer_scores_array.append(random_score)

    print(f"RUN: {run_no}, Non-random score: {non_random_score}, Random Score: {random_score}")

# Summarise the scores across all runs
non_random_avg_score = sum(non_random_answer_scores_array) / SIMULATION_RUNS
random_avg_score = sum(random_answer_scores_array) / SIMULATION_RUNS
print(f"Total runs: {SIMULATION_RUNS}")
print(f"Avg score for non-random answers (i.e. Answering C for every question): {non_random_avg_score}")
print(f"Avg score for random answers: {random_avg_score}")








"""Student scores program."""


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    subjects = scores_data[0].strip().split(",")
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
    subjects_scores = [
        ["Subject   :"] + [f"Student {i:>2}:" for i in range(1, 11)] + ["Minimum   :", "Maximum   :", "Average   :"]]
    for i, subject in enumerate(subjects):
        subject_scores = []
        for j in range(len(score_values)):
            subject_scores.append(score_values[j][i])
        subjects_scores.append([subject] + subject_scores + [min(subject_scores), max(subject_scores),
                                                             (sum(subject_scores) / len(subject_scores))])
    for i in range(len(subjects_scores[0])):
        for j in range(len(subjects_scores)):
            print(f"{subjects_scores[j][i]:>6}", sep='', end='')
        print()


main()

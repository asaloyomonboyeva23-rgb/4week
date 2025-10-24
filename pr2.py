def calculate_average(score1, score2, score3):
    return sum((score1, score2, score3)) / 3

def drop_lowest(score1, score2, score3):
    return (sum((score1, score2, score3)) - min(score1, score2, score3)) / 2

def calculate_weighted(assignments, midterm, final):
    return assignments * .3 + midterm * .3 + final * .4

def determine_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
    
def needs_improvement(current_avg, target_grade): # 'A’, ‘B’, ‘C’, ‘D’
    if target_grade == 'A':
        return current_avg < 90
    elif target_grade == 'B':
        return current_avg < 80
    elif target_grade == 'C':
        return current_avg < 70
    elif target_grade == 'D':
        return current_avg < 60
    else:
        return False
    
score1 = 85
score2 = 78
score3 = 92
midterm = 88
final = 82
target_grade = 'A'

regular_avg = calculate_average(score1, score2, score3)
avg_with_lowest_dropped = drop_lowest(score1, score2, score3)
better_avg = max(regular_avg, avg_with_lowest_dropped)
weighted_avg = calculate_weighted(better_avg, midterm, final)
student_needs_improvement = needs_improvement(weighted_avg, target_grade)
current_grade = determine_grade(weighted_avg)


print('STUDENT GRADE CALCULATOR')
print('========================================')
print(f"Assignment Scores: {score1}, {score2}, {score3}")
print(f"Midterm Score: {midterm}")
print(f'Final Score: {final}')
print('----------------------------------------')
print(f'Regular Assignment Average: {regular_avg:.2f}')
print(f"Average with Lowest Dropped: {avg_with_lowest_dropped:.2f}")
print(f'Using Better Average: {better_avg:.2f}')
print()
print(f'Weighted Course Average: {weighted_avg:.2f}')
print(f'Letter Grade: {current_grade}')
print()
print(f'Needs improvement for an \'{target_grade}\': {"Yes" if student_needs_improvement else "No"}')

points_needed = 0
if student_needs_improvement:
    if target_grade == 'A':
        points_needed = 90 - weighted_avg
    elif target_grade == 'B':
        points_needed = 80 - weighted_avg
    elif target_grade == 'C':
        points_needed = 70 - weighted_avg
    elif target_grade == 'D':
        points_needed = 60 - weighted_avg

print(f'Points needed: {points_needed:.2f}')
print(f'Already meets or exceeds \'{current_grade}\' grade requirement')

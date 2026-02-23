#Name : Radhika
#Roll No :iitp_aimltn_2602483
#Assignment : grade analyzer

# --- TASK 1: Calculate Averages ---
def process_scores(students):
    averages = {}
    for name, scores in students.items():
        # Add all scores and divide by how many scores there are
        avg = sum(scores) / len(scores)
        averages[name] = round(avg, 2)
    return averages

# --- TASK 2: Assign Letter Grades ---
def classify_grades(averages):
    results = {}
    for name, avg in averages.items():
        # Check the score against thresholds
        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        else:
            grade = "F"
        # Store the average and grade together in a pair
        results[name] = (avg, grade)
    return results

# --- TASK 3: Print the Report ---
def generate_report(classified_data, passing_avg=70):
    print("===== Student Grade Report =====")
    passed_count = 0
    
    for name, (avg, grade) in classified_data.items():
        # A simple 'if' to decide if they passed or failed
        if avg >= passing_avg:
            status = "PASS"
            passed_count += 1
        else:
            status = "FAIL"
        
        # {name:<10} makes the name take 10 spaces so the bars | line up
        print(f"{name:<10} | Avg: {avg:<8.2f} | Grade: {grade} | Status: {status}")

    # Calculate failed count by subtracting passes from the total
    total = len(classified_data)
    print("================================")
    print(f"Total Students : {total}")
    print(f"Passed         : {passed_count}")
    print(f"Failed         : {total - passed_count}")

# --- THE START BUTTON (Execution) ---
# We define the data and call the functions one by one
if __name__ == "__main__":
    # 1. Our raw data
    my_students = {
        "Alice": [90, 85, 92],
        "Bob": [78, 80, 75],
        "Clara": [60, 65, 70]
    }

    # 2. Step-by-step processing
    student_averages = process_scores(my_students)
    final_grades = classify_grades(student_averages)
    
    # 3. Show the final result
    generate_report(final_grades)
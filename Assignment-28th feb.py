import matplotlib.pyplot as plt

subjects = ['Math', 'Science', 'English', 'CS', 'History']
hours = [10, 8, 6, 12, 4]

plt.figure()
plt.bar(subjects, hours)
plt.title("Study Hours per Subject")
plt.xlabel("Subjects")
plt.ylabel("Hours")
plt.show()

plt.figure()
plt.pie(hours, labels=subjects, autopct='%1.1f%%')
plt.title("Study Distribution")
plt.show()

marks = [45, 50, 60, 65, 70, 75, 80, 85, 90, 95]
plt.figure()
plt.hist(marks)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

'''The bar chart shows that the student spends the most time on Computer Science and the least time on History. This indicates a stronger focus on technical subjects.

The pie chart highlights that a major portion of study time is dedicated to Math and Computer Science, showing priority areas.

The histogram of marks shows that most scores lie between 70 and 90, indicating good academic performance overall.

From these graphs, we can conclude that higher study time in certain subjects may lead to better performance, suggesting a positive relationship between effort and results.'''
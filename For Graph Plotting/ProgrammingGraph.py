import  matplotlib.pyplot as plt
lang = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [28, 34, 26, 40, 21]
plt.title("Programming")
plt.xlabel('X : axis')
plt.ylabel('Y : axis')
plt.bar(lang, students)
plt.grid()
plt.show()
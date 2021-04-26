import matplotlib.pyplot as plt
import random
import math


def pi_value_estimator(iteration, pi_values, interactions_seq):
    count_inside = 0
    in_X, in_Y, out_X, out_Y = [], [], [], []

    interactions_seq.append(iteration)

    # x and y values by using random generator
    for count in range(0, iteration):
        # x = random.random()
        # y = random.random()
        x = 2 * (random.random() - 0.5)
        y = 2 * (random.random() - 0.5)
        d = math.sqrt(x ** 2 + y ** 2)
        if d < 1:
            count_inside += 1
            in_X.append(x)
            in_Y.append(y)
        else:
            out_X.append(x)
            out_Y.append(y)
    count += 1
    pi_value = (4.0 * count_inside / count)

    pi_values.append(pi_value)

    # square
    rectangle = plt.Rectangle((-1, -1), 2, 2, ec="black", fill=False)
    # circle
    circle = plt.Circle((0, 0), 1, ec="yellow", fill=False)

    plt.gca().add_patch(rectangle)
    plt.gca().add_patch(circle)

    # plotting
    plt.scatter(in_X, in_Y, color='red', marker=".")
    plt.scatter(out_X, out_Y, color='blue', marker=".")

    plt.axis("equal")
    plt.show()

    return pi_value


pi_values = []
interactions_seq = []

print("For 10 values, Estimated Pi Value is " + str(pi_value_estimator(10, pi_values, interactions_seq)))
print("For 500 values, Estimated Pi Value is  " + str(pi_value_estimator(500, pi_values, interactions_seq)))
print("For 1000 values, Estimated Pi Value is  " + str(pi_value_estimator(1000, pi_values, interactions_seq)))
print("For 5000 values, Estimated Pi Value is " + str(pi_value_estimator(5000, pi_values, interactions_seq)))
print("For 10000 values, Estimated Pi Value is " + str(pi_value_estimator(10000, pi_values, interactions_seq)))
print("For 50000 values, Estimated Pi Value is  " + str(pi_value_estimator(50000, pi_values, interactions_seq)))
print("For 80000 values, Estimated Pi Value is " + str(pi_value_estimator(80000, pi_values, interactions_seq)))
print("For 100000 values, Estimated Pi Value is  " + str(pi_value_estimator(100000, pi_values, interactions_seq)))
print("For 200000 values, Estimated Pi Value is  " + str(pi_value_estimator(500000, pi_values, interactions_seq)))


print(pi_values)
print(interactions_seq)
print("Line chart:")

#line graph to compare the accuracy of pi value

plt.plot(pi_values,interactions_seq)
plt.xlabel('Pi Value')
plt.ylabel('Simulations')
plt.show()
def example_function(param1, param2, param3, param4):
    
    results = []
    if param1 > 10 and param2 < 5:
        for i in range(5):
            if i % 2 == 0:
                results.append("Even number")
            else:
                results.append("Odd number")
    else:
        results.append("Condition not met")

    return results

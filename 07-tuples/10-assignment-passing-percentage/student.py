def passing_percentage(grades):
    passed = 0
    for g in grades:
        if g >= 10:
            passed += 1
    
    return passed / len(grades) * 100
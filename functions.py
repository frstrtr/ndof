def unlimited_arguments(*args, **keyword_args):
    print(keyword_args)
    for k, argument in keyword_args.items():
        print(k, argument)


unlimited_arguments(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, name='Max', age=29)

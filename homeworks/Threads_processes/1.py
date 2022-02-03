import threading


def threads_count():
    return threading.active_count()


def user_name(name):
    print(f"Hello, {name}")


t1 = threading.Thread(target=user_name, args=['Alex'])
t2 = threading.Thread(target=user_name, args=['Oleg'])

user_name('Artur')
print(f'Threads count before start: {threads_count()}')

t1.start()
t2.start()

print(f'Threads count before join: {threads_count()}')

t1.join()
t2.join()

print(f'Threads count: {threads_count()}')
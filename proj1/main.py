from stack import *

def main():
    stc = Stack()
    bucket = Stack(1, 'fds', 4.123)
    bucket.append(21, '313')
    bucket.append()
    print(bucket.length())
    print(bucket.pop())
    print(bucket.length())
    print(bucket.get_top())
    print(bucket.set_top(12121))
    

if __name__ == '__main__':
    main()
def main():
    try:
        with open('test.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except:
        print(f"e")   
    input() 
if __name__ == '__main__':
    main()
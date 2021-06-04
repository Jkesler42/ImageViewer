def run(filename):
    with open(filename, 'rb') as f:
        f_bin_data = f.read()
        print(f_bin_data)

if __name__ == '__main__':
    run(R'C:\users\jake\documents\projects\python\ImageViewer\test.png')

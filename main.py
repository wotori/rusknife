from tools.walker import Walker

if __name__ == '__main__':
    walker = Walker('/media/wotori/Media/iPhone11')
    walker.collect_data()
    print(walker.data_bag)

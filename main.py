from tools.walker import Walker

if __name__ == '__main__':
    walker = Walker('/media/wotori/Media/iPhone11')
    walker.collect_data()
    print(walker.data_bag)

# TODO: просканировать все файлы, получить exif.
# TODO: на основе exif создать список дат и структуру папок

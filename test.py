import imageio
import os


path = '/home/stalin/Pictures/'
filenames = os.listdir(path)
try:
    filenames.index('result.gif')
except ValueError:
    print('not exists!')
else:
    filenames.remove('result.gif')
filenames.sort(key=lambda file: int(file[:-len('.png')]))


def write():
    with imageio.get_writer(path + 'result.gif', mode='I', duration=0.1) as writer:
        for filename in filenames:
            if filename.endswith('.png'):
                image = imageio.imread(path + filename)
                writer.append_data(image)


if __name__ == '__main__':
    write()

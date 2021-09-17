from PIL import Image
import glob
import os


def expand2square(pil_img: Image, background_color: tuple) -> Image:
    """入力画像を正方形に変換する

    Parameters:
    ----------
    pil_img : Image
        入力画像
    background_color : tuple
        背景色をtuple型で指定

    Returns:
    ----------
    result
        正方形の出力画像

    """
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result


def padding_resize(file_path: str, width: int, height: int) -> Image:
    """入力パスの画像をPIL.Imageに変換し，正方形に変換後，リサイズを行う

    Parameters:
    ----------
    file_path : str
        入力画像のファイルパス
    width : int
        変換後の画像の横幅
    height : int
        変換後の画像の縦幅

    Returns:
    ----------
    im_resize : Image
        リサイズされたPIL.Image

    """
    im = Image.open(file_path)
    im_new = expand2square(im, (0, 0, 0))
    im_resize = im_new.resize((width, height))
    return im_resize


def arrange_images_glob(input_folder: str, output_img: str,
                        row: int, col: int, width=300, height=300) -> None:
    file_path = []
    for file_name in glob.glob(input_folder+"/*.png"):
        file_path.append(file_name)
    file_path = file_path[76:101]
    dst = Image.new('RGB', (row*width, col*height))
    i = 0
    for y in range(col):
        for x in range(row):
            im = padding_resize(file_path[i], width, height)
            dst.paste(im, (x*width, y*height))
            i += 1
    dst.save(output_img)


def arrange_images(input_folder: str, output_img: str,
                   img_num_start: int, img_num_end: int,
                   row=5, col=5, width=300, height=300) -> None:
    """複数枚の画像を並べた画像を出力する
    画像ファイル名は「1.png」のように{int}.pngである必要がある

    Parameters:
    ----------
    input_folder : str
        画像が保存されているフォルダー名を指定する
    output_img : str
        出力ファイル名
    row : int
        横に画像を何枚並べるか整数値で指定する
    col : int
        縦に画像を何枚並べるか整数値で指定する
    width : int
        一枚の画像の横幅の大きさの指定
    height : int
        一枚の画像の高さの指定

    Returns:
    ----------
    Image
        並べた画像ファイルが出力される
        画像が存在しなかったとき黒の画像が貼り付けられる
    """

    file_path = []
    black = "black.png"
    for i in range(img_num_start, img_num_end+1):
        file_name = input_folder+"/{}.png".format(i)
        if os.path.exists(file_name):
            file_path.append(file_name)
        else:
            file_path.append(black)

    dst = Image.new('RGB', (row*width, col*height))
    i = 0
    for y in range(col):
        for x in range(row):
            if i <= len(file_path):
                im = padding_resize(file_path[i], width, height)
            else:
                im = padding_resize(black, width, height)
            dst.paste(im, (x*width, y*height))
            i += 1
    dst.save(output_img)


def arrange_images2(input_folder: str, output_img: str,
                   row=5, col=5, width=300, height=300) -> None:
    """複数枚の画像を並べた画像を出力する
    画像ファイル名は「1.png」のように{int}.pngである必要がある

    Parameters:
    ----------
    input_folder : str
        画像が保存されているフォルダー名を指定する
    output_img : str
        出力ファイル名
    row : int
        横に画像を何枚並べるか整数値で指定する
    col : int
        縦に画像を何枚並べるか整数値で指定する
    width : int
        一枚の画像の横幅の大きさの指定
    height : int
        一枚の画像の高さの指定

    Returns:
    ----------
    Image
        並べた画像ファイルが出力される
        画像が存在しなかったとき黒の画像が貼り付けられる
    """
    black = "black.png"
    dst = Image.new('RGB', (row*width, col*height))
    i = 0
    for y in range(col):
        for x in range(row):
            file_path = input_folder + "/sr_{}_sc_{}.png".format(round(y*0.2+0.4, 1), round(x*0.2+0.2, 1))
            if not os.path.exists(file_path):
                file_path = black

            if i <= len(file_path):
                im = padding_resize(file_path, width, height)
            else:
                im = padding_resize(black, width, height)
            dst.paste(im, (x*width, y*height))
            i += 1
    dst.save(output_img)


def arrange_images3(input_folder: str, output_img: str,
                   row=5, col=5, width=300, height=300) -> None:
    """複数枚の画像を並べた画像を出力する
    画像ファイル名は「1.png」のように{int}.pngである必要がある

    Parameters:
    ----------
    input_folder : str
        画像が保存されているフォルダー名を指定する
    output_img : str
        出力ファイル名
    row : int
        横に画像を何枚並べるか整数値で指定する
    col : int
        縦に画像を何枚並べるか整数値で指定する
    width : int
        一枚の画像の横幅の大きさの指定
    height : int
        一枚の画像の高さの指定

    Returns:
    ----------
    Image
        並べた画像ファイルが出力される
        画像が存在しなかったとき黒の画像が貼り付けられる
    """

    black = "black.png"
    dst = Image.new('RGB', (row*width, col*height))
    i = 0
    for y in range(col):
        for x in range(row):
            #file_path = input_folder + "/half/half_sr_{}_sc_{}.png".format(round(y*0.1+0.2, 1), round(x*0.1+0.1, 1))
            file_path = input_folder + "/half_sr_{}_sc_{}.png".format(round(y*0.2+0.4, 1), round(x*0.2+0.2, 1))
            if not os.path.exists(file_path):
                file_path = black

            if i <= len(file_path):
                im = padding_resize(file_path, width, height)
            else:
                im = padding_resize(black, width, height)
            dst.paste(im, (x*width, y*height))
            i += 1
    dst.save(output_img)


def func(start: int, end: int):
    arrange_images("./",
                   "./compleat_{}_{}.png".format(start, end),
                   start, end, row=5, col=5, width=600, height=600)

def func2(i):
    arrange_images2("./Grid_100/{}".format(i),
                    "Arrange_img_grid/{}.png".format(i), row=4, col=4)
    arrange_images3("./Grid_100/{}".format(i),
                    "Arrange_img_grid/half_{}.png".format(i), row=4, col=4)


if __name__ == '__main__':
    arrange_images("./",
                   "./compleat_{}_{}.png".format(1, 50),
                   1, 50, row=10, col=5, width=600, height=600)
    arrange_images("./",
                   "./compleat_{}_{}.png".format(51, 100),
                   51, 100, row=10, col=5, width=600, height=600)

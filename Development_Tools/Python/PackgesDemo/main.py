from IPython import embed

import package

if __name__ == '__main__':
    A = package.ClassA()
    A.func()

    B = package.ClassA()
    B.func()

    C = package.ClassA()
    C.func()

    # 这里演示yapf进行代码格式化功能，不过即将被vscode弃用，请选择其他格式化工具
    a = [1, 1, 1]
    print(
        '*********************************************************************************'
    )

    embed()

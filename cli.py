import argparse

parser = argparse.ArgumentParser(
    prog='PointValidator',
    description='Validates a given point x, y',
    epilog='Text at the bottom of help'
)
parser.add_argument('x', type=int, help="X value different to zero")  
parser.add_argument('y', type=int, help="Y value different to zero")  

args = parser.parse_args()

x = args.x
y = args.y

print(x)
print(y)
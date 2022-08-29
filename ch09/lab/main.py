from Rectangle import Rectangle
from Surface import Surface

def main():
    print("###################  Test #1: Testing Rectangle Class ####################")
    r = Rectangle(10, 10, 10, 10)
    assert((r.x, r.y, r.height, r.width) == (10,10,10,10))
    r = Rectangle(-1, 1, 1, 1)
    assert((r.x, r.y, r.height, r.width) == (0,1,1,1))
    r = Rectangle(1, -1, 1, 1)
    assert((r.x, r.y, r.height, r.width) == (1,0,1,1))
    r = Rectangle(1, 1, -1, 1)
    assert((r.x, r.y, r.height, r.width) == (1,1,0,1))
    r = Rectangle(1, 1, 1, -1)
    assert((r.x, r.y, r.height, r.width) == (1,1,1,0))
    print(r)
    print("Test Complete!")

    print("###################  Test #2: Test Surface Class ####################")
    s = Surface("myimage.png", 10, 10, 10, 10)
    assert((s.rect.x, s.rect.y, s.rect.height, s.rect.width) == (10,10,10,10))
    assert((s.getRect().x, s.getRect().y, s.getRect().height, s.getRect().width) == (10,10,10,10))
    assert(s.image == "myimage.png")
    print("Test Complete!")

main()

from DiamondTrap import King
from S1E9 import Stark
from S1E7 import Baratheon, Lannister


def ex00():
    """Tester for the Stark class."""
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)
    # hodor = Character("hodor")


def ex01():
    """Tester for the Baratheon and Lannister classes."""
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(
        f"""
Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}
"""
    )


def ex02():
    """Tester the King class."""
    joffrey = King("Joffrey")
    print(joffrey.__dict__)
    joffrey.set_eyes("blue")
    joffrey.set_hairs("light")
    print(joffrey.get_eyes())
    print(joffrey.get_hairs())
    print(joffrey.__dict__)


def main():
    """main function to run the testers for the exercises."""
    ex00()

    print()
    print()
    print()

    ex01()

    print()
    print()
    print()

    ex02()


if __name__ == "__main__":
    main()

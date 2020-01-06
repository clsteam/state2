# state2
Python3 beautify code with state mode
###### reference::
1.[state PyPI](https://pypi.org/project/state/0.1.2dev-r2/#files)

2.

### what is state mode？
* The group state pattern is to allow an object to change its behavior when its internal state changes, but the object looks like it has changed its class. The state mode is mainly used to control the conditional expression of an object's state if it is too complicated. It can transfer the state judgment logic to a series of classes representing different states, and then simplify the complicated judgment logic.
Thanks to the dynamic nature of the Python language, the Python implementation of the state pattern is much simpler than versions of languages such as C ++. 

### useage：
1. For example, a person's daily life is different on weekdays and Sundays.
```
def workday():
    print ' work hard!'
def weekend():
    print ' play harder!'
class People(object):
    pass people=People()
while True:
    for 1 in xrange(1,8):
        if i==6:
            people.day=weekend
        if i==1:
            people.day=workday
        people. day()
```
2.Running the above code, the output is as follows:
```
work hard!
work hard!
work hard!
work hard!
work hard!
play harder!
play harder!
...
```
3.In this way, the state pattern is achieved by replacing the instance methods (that is, behaviors) under different conditions.
```
from state2 import State, stateful, behavior, switch
@stateful
class People (object):
    class workday (State):
        default=True 
        @behavior 
        def day(aelf):
            print ' work hard.'
    class weekend(State): 
        @behavior  
        def day(self): 
            print ' play harder!'

people=People()
while True:.·
    for i in range(1,8): 
        if i == 6: 
            switch (people, People. Weekend)
        if i == 1: 
            switch (people, People. Workday)
        people. day()
```

* how about it? Does it feel longer than the code before applying the pattern? This is because the example is too simple. I will show you more examples closer to real business needs later. Now let's press this table and look at people.day0 in the last row. People is an instance of People, but People does not define the day0 method? In order to resolve this doubt, we need to look at it from the beginning.
* The first is the @stateful modification function, which contains many "black magic". The most important one is to override the _getattr_0 method of the decorated class so that the instance of People can call the method of the current state class. Instances of classes modified by @stateful are stateful. You can use currO to query the current state, or you can use switch0 to switch states. If you continue to look down, you can see that the Workday class continues from the State class. This State class is also from the state package. Subclasses derived from it can use the begin_ and __end__ state transition protocols. By overloading these two Protocol, subclasses can customize the initialization and cleanup of the host (in this case, people) when entering and leaving the current state. For a @stateful class, there is a default state (that is, the first state after its instance is initialized), which is identified by the default attribute of the class definition, and the class with default set to True becomes the default state. The @behavior modifier is used to modify the methods of the state class. In fact, it is an alias for the built-in function staticmethod. Why implement the methods of the state class as static methods? Because the principle of the state package is that the state class has only behaviors and no state (the state is stored on the host), which can better achieve code reuse. So since the day0 method is static, why does it have a self parameter? This is actually because self is not a keyword in Python. Using self here helps to understand that the host of the state class is an instance of People.

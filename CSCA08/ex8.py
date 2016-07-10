''' The switches that are on would be 0,0+1,1+3,4+5,9+7,16+9 ......'''


class LightSwitch:
    '''class that represents a Light Switch by using a boolean
       with true representing on and false representing off
    '''

    def __init__(self, state=None):
        '''
        (LightSwitch, String) -> NoneType
        creates a new light switch. if state is "on" then the switch is on
        if the state is "off" then the switch is off
        '''

        self._state = False

        if (state == "on"):
            self._state = True

    def turn_on(self):
        '''
        (LightSwitch) -> NoneType
        Sets the state of the object to on
        '''
        self._state = True

    def turn_off(self):
        '''
        (LightSwitch) -> NoneType
        sets the state of the object to off
        '''
        self._state = False

    def flip(self):
        '''
        (LightSwitch) -> NoneType
        If the switch is on the switch turns off
        and vice versa
        '''
        if (self._state):
            self._state = False

        elif (not self._state):
            self._state = True

    def __str__(self):
        '''
        (LightSwitch) -> String
        returns a string representation of a LightSwitch
        in this case if the switch is on then it returns "I am on"
        and if the switch is off then it returns "I am off"

        >>>x = LightSwitch("on")
        >>>str(x)
        "I am on"

        >>>x = LightSwitch("off")
        >>>str(x)
        "I am off"
        '''
        res = ""

        if (self._state):
            res = "I am on"
        else:
            res = "I am off"

        return res

    def on_or_off(self):
        '''
        (LightSwitch) -> boolean
        returns whether the switch is on(True) or off(False)

        >>>x = LightSwitch("on")
        >>>x.on_or_off()
        True

        >>>x = LightSwitch("off")
        >>>x.on_or_off()
        False
        '''
        return self._state


class SwitchBoard:
    '''creates a switch board of LightSwitch objects'''

    def __init__(self, num):
        '''
        (Switchboard,integer) -> NoneType
        creates an SwitchBoard that holds num number
        of LightSwitch objects
        '''
        self._array_of_switches = []

        for a in range(0, num):
            self._array_of_switches.append(LightSwitch())

    def which_switch(self):
        '''
        (SwitchBoard) -> List
        returns a list of all the LightSwitches that are on
        '''
        arr = []

        for index in range(0, len(self._array_of_switches)):
            if (self._array_of_switches[index].on_or_off()):
                arr.append(index)

        return arr

    def __str__(self):
        '''
        (SwitchBoard) -> String
        returns a string representation of SwitchBoard
        in the form of "The following switches are on: "
        plus all the switches that are on
        '''
        res = "The following switches are on: "
        arr = self.which_switch()
        for integer in arr:
            res += (" " + str(integer))

        return str(res)

    def flip(self, num):
        '''
        (SwitchBoard, integer) -> NoneType
        flips the LightSwitch at index num
        '''
        if (num < len(self._array_of_switches) and num >= 0):
            self._array_of_switches[num].flip()

    def flip_every(self, num):
        '''
        (SwitchBoard, integer) -> NoneType
        flips every LightSwitch every num
        '''
        for a in range(0, len(self._array_of_switches), num):
            self._array_of_switches[a].flip()

    def reset(self):
        '''
        (SwitchBoard) -> NoneType
        sets all LightSwitches to off
        '''
        for light in self._array_of_switches:
            light.turn_off()

# if(__name__ == "__main__"):
#    x = SwitchBoard(1024)
#    for a in range(1,1024):
#        x.flip_every(a)
#        print("itr",a,x)

    '''
    I got it right!
    this pattern exists because each
    '''
''' The switches that are on would be 0,0+1,1+3,4+5,9+7,16+9 ......'''


class LightSwitch:
    '''class that represents a Light Switch by using a boolean
       with true representing on and false representing off
    '''

    def __init__(self, state=None):
        '''
        (LightSwitch, String) -> NoneType
        creates a new light switch. if state is "on" then the switch is on
        if the state is "off" then the switch is off
        '''

        self._state = False

        if (state == "on"):
            self._state = True

    def turn_on(self):
        '''
        (LightSwitch) -> NoneType
        Sets the state of the object to on
        '''
        self._state = True

    def turn_off(self):
        '''
        (LightSwitch) -> NoneType
        sets the state of the object to off
        '''
        self._state = False

    def flip(self):
        '''
        (LightSwitch) -> NoneType
        If the switch is on the switch turns off
        and vice versa
        '''
        if (self._state):
            self._state = False

        elif (not self._state):
            self._state = True

    def __str__(self):
        '''
        (LightSwitch) -> String
        returns a string representation of a LightSwitch
        in this case if the switch is on then it returns "I am on"
        and if the switch is off then it returns "I am off"

        >>>x = LightSwitch("on")
        >>>str(x)
        "I am on"

        >>>x = LightSwitch("off")
        >>>str(x)
        "I am off"
        '''
        res = ""

        if (self._state):
            res = "I am on"
        else:
            res = "I am off"

        return res

    def on_or_off(self):
        '''
        (LightSwitch) -> boolean
        returns whether the switch is on(True) or off(False)

        >>>x = LightSwitch("on")
        >>>x.on_or_off()
        True

        >>>x = LightSwitch("off")
        >>>x.on_or_off()
        False
        '''
        return self._state


class SwitchBoard:
    '''creates a switch board of LightSwitch objects'''

    def __init__(self, num):
        '''
        (Switchboard,integer) -> NoneType
        creates an SwitchBoard that holds num number
        of LightSwitch objects
        '''
        self._array_of_switches = []

        for a in range(0, num):
            self._array_of_switches.append(LightSwitch())

    def which_switch(self):
        '''
        (SwitchBoard) -> List
        returns a list of all the LightSwitches that are on
        '''
        arr = []

        for index in range(0, len(self._array_of_switches)):
            if (self._array_of_switches[index].on_or_off()):
                arr.append(index)

        return arr

    def __str__(self):
        '''
        (SwitchBoard) -> String
        returns a string representation of SwitchBoard
        in the form of "The following switches are on: "
        plus all the switches that are on
        '''
        res = "The following switches are on: "
        arr = self.which_switch()
        for integer in arr:
            res += (" " + str(integer))

        return str(res)

    def flip(self, num):
        '''
        (SwitchBoard, integer) -> NoneType
        flips the LightSwitch at index num
        '''
        if (num < len(self._array_of_switches) and num >= 0):
            self._array_of_switches[num].flip()

    def flip_every(self, num):
        '''
        (SwitchBoard, integer) -> NoneType
        flips every LightSwitch every num
        '''
        for a in range(0, len(self._array_of_switches), num):
            self._array_of_switches[a].flip()

    def reset(self):
        '''
        (SwitchBoard) -> NoneType
        sets all LightSwitches to off
        '''
        for light in self._array_of_switches:
            light.turn_off()

# if(__name__ == "__main__"):
#    x = SwitchBoard(1024)
#    for a in range(1,1024):
#        x.flip_every(a)
#        print("itr",a,x)

    '''
    I got it right!
    this pattern exists because each
    '''

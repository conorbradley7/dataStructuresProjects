#Conor Bradley
#119408464
#CS2515 ca01

class Track:
    def __init__(self,name,artiste,timesplayed=0):
        self._name = name
        self._artiste = artiste
        self._timesplayed = timesplayed
        self._prev = None
        self._next = None

    def __str__(self):
        return("%s; %s (%d)" %(self._name, self._artiste,self._timesplayed))

    def get_name(self):
        return self._name

    def get_artiste(self):
        return self._artiste

    def play(self):
        self._timesplayed += 1
        return self



class PyToonz:
    def __init__(self):
        self._head = None       #Using pointers for head and tail
        self._tail = None
        self._current = None

    def __str__(self):
        ans = "Playlist: \n"
        pointer = self._head
        while pointer != None:
            if pointer == self._current:
                ans += "==> "
            ans += "%s; %s (%d) \n" %(pointer._name, pointer._artiste, pointer._timesplayed)
            pointer = pointer._next
        return ans

    def length(self):
        size = 0
        pointer = self._head
        while pointer != None:
            pointer = pointer._next
            size += 1
        return size

    def get_current(self):
        if self.length() == 0:      #If list empty, reset current to None.
            self._current = None
        return self._current

    def add_track(self, track):
        if isinstance(track, Track):
            if self.length() == 0:
                self._head = track
                self._tail = track
                self._current = track
            else:
                track._prev = self._tail
                self._tail._next = track
                self._tail = track
        else:
            print("ERROR TRACK INPUTTED NOT INSTANCE OF TRACK CLASS \nTrack NOT added\n")

    def add_after(self,track):
        if isinstance(track, Track):
            curr_track = self.get_current()
            if curr_track == self._tail:
                self.add_track(track)
            else:
                track._next = curr_track._next
                curr_track._next._prev = track
                track._prev = curr_track
                curr_track._next = track
        else:
            print("ERROR TRACK INPUTTED NOT INSTANCE OF TRACK CLASS \nTrack NOT added\n")

    def remove_current(self):
        if self.length() != 0:
            del_track = self.get_current()
            #del_track.timesplayed = 0          Wasn't sure if you wanted to reset timesplayed to 0 if deleted from playlist
            self.next_track()
            if del_track == self._head:
                if del_track._next == None:     #List will be empty in this case
                    self._head = None
                    self._tail = None
                    self._current = None
                else:
                    self._head = del_track._next
                    self._head._prev = None
            elif del_track == self._tail:
                self._tail = del_track._prev
                self._tail._next = None
            else:
                del_track._prev._next = del_track._next
                del_track._next._prev = del_track._prev
            del_track._prev = None
            del_track._next = None
        else:
            print("Error! Playlist already Empty! \n")


    def next_track(self):
        curr_track = self.get_current()
        if curr_track == self._tail:
            self._current = self._head
        else:
            self._current = curr_track._next

    def prev_track(self):
        curr_track = self.get_current()
        if curr_track == self._head:
            self._current = self._tail
        else:
            self._current = curr_track._prev

    def reset(self):
        self._current = self._head

    def play(self):
        track = self.get_current()
        print("Now Playing: "+str(track.play())+"\n")

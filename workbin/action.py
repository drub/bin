#! /usr/bin/python
# ! /opt/local/bin/python

import sys
import argparse

progVersion = "3.0"
dashLineLength = 70

debug = 2
debug = 3
debug = 0
debug = 1


# debug = 4

# Template version 1.0

def dashline(lnLen, char="-"):
    # ------------------------------------------------------------
    print char * lnLen


def openFile(fname):
    # ------------------------------------------------------------
    # print '-- File to open: %s ' % fname  #debug
    try:
        FH = open(fname)
        if debug > 0:
            print '-- File opened: %s' % fname  # debug
    except IOError:
        print "ERROR: Input file not found: ", fname
        return False
    else:
        return FH


class Record:
    # ------------------------------------------------------------

    def _foo():
        # Silly test of scope rules.
        pass

    def __init__(self, line, lineCount, date):
        # --------------------------------------------------

        self.lineNo = lineCount
        self.openDate = date

        self.recordType = "UNDEFINED"
        self.recordVer = "UNDEFINED"
        self.owner = "UNDEFINED"
        self.desc = "UNDEFINED"
        self.state = "UNDEFINED"
        self.startDate = "UNDEFINED"
        self.completeDate = "UNDEFINED"
        self.completeDesc = "UNDEFINED"
        self.eventName = "UNDEFINED"
        self.date = "UNDEFINED"
        self.time = "UNDEFINED"
        self.timeZone = "UNDEFINED"
        self.day = "UNDEFINED"
        self.valid = "UNDEFINED"

        self.actionRecordType = "A"
        self.eventRecordType = "E"
        self.dateRecordType = "D"
        self.commentRecordType = "comment"
        self.emptyRecordType = "empty"
        self.textRecordType = "text"

        fields = line.split("::")
        fieldCount = len(fields)
        if debug > 1:
            print "++ init fieldCount: ", fieldCount  # debug
            print "++ init fields: ", fields  # debug

        if fieldCount == 1:
            lineTokens = line.split()
            # print("++ lineTokens: %s" % lineTokens)	#debug
            if lineTokens == []:
                # print ("++ Empty line.")	#debug
                self.recordType = self.emptyRecordType
            # print("++ lineTokens[0]: " + lineTokens[0])	#debug
            elif lineTokens[0] == "#":
                self.recordType = self.commentRecordType
            else:
                self.recordType = self.textRecordType

        if fieldCount > 1:

            # print "++ length: ", len(fields)   #debug

            self.recordType = fields[0]

            # Action records
            if self.recordType == self.actionRecordType:
                self.recordVer = fields[1]

                if debug > 0:
                    print "++ Action record found"
                    print "   ++ self.lineNo ....... ", self.lineNo  # debug
                    print "   ++ self.recordVer .... ", self.recordVer  # debug

                if (self.recordVer == "2.0") or (self.recordVer == "1.1") \
                        or (self.recordVer == "1.2"):
                    try:
                        self.owner = fields[2]
                        self.desc = fields[3]
                        self.state = fields[4]
                        self.completeDate = fields[5]
                        self.completeDesc = fields[6]
                    except (IndexError):
                        dashline(dashLineLength)
                        print "[%05i] ERROR: Malformed record. Type: %s   Ver: %s" \
                              % (self.lineNo, self.recordType, self.recordVer)
                        print "[%05i] %s" % (self.lineNo, line)
                elif (self.recordVer == "3.0"):
                    try:
                        self.state = fields[2]
                        self.startDate = fields[4]
                        self.completeDesc = fields[5]
                    except (IndexError):
                        dashline(dashLineLength)
                        print "[%05i] ERROR: Malformed record. Type: %s   Ver: %s" \
                              % (self.lineNo, self.recordType, self.recordVer)
                        print "[%05i] %s" % (self.lineNo, line)

                else:
                    # There was no version indicator in version 1 records.
                    try:
                        self.recordVer = "1.0"
                        self.owner = fields[1]
                        self.desc = fields[2]
                        self.state = fields[3]
                        self.completeDate = fields[4]
                    except (IndexError):
                        dashline(dashLineLength)
                        print "[%05i] ERROR: Malformed record. Type: %s   Ver: %s" \
                              % (self.lineNo, self.recordType, self.recordVer)
                        print "[%05i] %s" % (self.lineNo, line)

                if debug > 0:
                    print "   ++ self.state ........ ", self.state  # debug

            # Event records
            elif self.recordType == self.eventRecordType:
                self.eventName = fields[3]

            # Date records
            elif self.recordType == self.dateRecordType:
                dateTokens = fields[3].split('-')
                if debug == 3:
                    print "++ Date record:     ", dateTokens
                    self.date = dateTokens[0]
                    self.time = dateTokens[1]
                    self.timeZone = dateTokens[2]

    def display(self):
        # --------------------------------------------------
        print "lineNo ................. %s" % self.lineNo
        print "recordType ............. %s" % self.recordType
        print "recordVer .............. %s" % self.recordVer
        print "owner .................. %s" % self.owner
        print "Desc ................... %s" % self.desc
        print "state .................. %s" % self.state
        print "openDate ............... %s" % self.openDate
        print "completeDate ........... %s" % self.completeDate
        print "completeDesc ........... %s" % self.completeDesc
        print "date ................... %s" % self.date
        print "time ................... %s" % self.time
        print "timeZone ............... %s" % self.timeZone
        print "day .................... %s" % self.day
        '''
        if debug > 1 :
            print ([self.recordType, \
                    self.recordVer, \
                    self.owner, \
                    self.desc, \
                    self.state, \
                    self.completeDate, \
                    self.completeDesc \
                ])
                '''

    def iscomplete(self):
        # --------------------------------------------------
        pass


# TODO todo
#

def main():
    # ------------------------------------------------------------

    typeAction = "A"
    typeDate = "D"
    typeEmpty = "empty"
    typeText = "text"
    typeComment = "comment"
    stateIncomplete = "I"
    stateComplete = "C"
    currentDate = "UNDEFINED"

    parser = argparse.ArgumentParser(description="List actions",
                                     version=progVersion)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-i', action='store_true',
                       help='Display incomplete actions')
    group.add_argument('-n', action='store_true',
                       help='Display actions that will not be completed')
    group.add_argument('-c', action='store_true',
                       help='Display completed actions')
    prog_args = parser.parse_args()

    if debug > 0:
        print ('++++++++++++++++++++++++++++++++++++++')
        print ('+++++ Debug Mode +++++ Level = %i +++++' % debug)
        print ('++++++++++++++++++++++++++++++++++++++')

    inputFileName = "junk"
    #inputFileName = "/Users/thedrub/cloud_storage/Dropbox (cPrime Inc.)/for David Bacon/cPrime.txt"
    inputFileName = "/Users/thedrub/Sync/doc/journal/work/journal_work.txt"
    inputFileFH = openFile(inputFileName)

    if debug > 0:
        print ('%15s ..... %s' % ("i", prog_args.i))
        print ('%15s ..... %s' % ("n", prog_args.n))
        print ('%15s ..... %s' % ("c", prog_args.c))

    lineCount = 0
    # for line in sys.stdin :
    for line in inputFileFH:

        lineCount += 1
        line = line.rstrip()

        if debug > 1:
            print "[%05i] %s" % (lineCount, line)

        rec = Record(line, lineCount, currentDate)
        if rec.recordType == typeEmpty:
            if debug > 1:
                print "[%05i] %s" % (lineCount, "++ Empty line")

        elif rec.recordType == typeText:
            if debug > 1:
                print "[%05i] %s" % (lineCount, "++ Text line")

        elif rec.recordType == typeDate:
            currentDate = rec.date
            if debug > 1:
                print "[%05i] %s: %s" % (lineCount, "++ New date", currentDate)

        # Display completed actions
        elif (rec.recordType == typeAction) and (prog_args.c) and \
                (rec.state == stateComplete):

            dashline(dashLineLength)
            if debug > 1:
                print "[%05i] %s" % (lineCount, "++ Complete action")

            print "[%05i] Owner: %-20s Open: %s   Closed: %s" % (rec.lineNo, rec.owner, rec.openDate, rec.completeDate)
            print "        Desc:  %s" % (rec.desc)

        # Display incomplete actions
        elif (rec.recordType == typeAction) and (prog_args.i) and \
                (rec.state == stateIncomplete):

            dashline(dashLineLength)
            if debug > 1:
                print "[%05i] %s" % (lineCount, "++ Incomplete action")
                print "[%05i] ++ Open date: %s" % (lineCount, rec.openDate)
                print "[%05i] ++ Complete date: %s" % (lineCount, rec.completeDate)
                print "[%05i] ++ Line number: %i" % (lineCount, rec.lineNo)

            # TODO: Make the following formatting lines a function call.
            print "[%05i] Owner: %-20s Open: %s" % (rec.lineNo, rec.owner, rec.openDate)
            print "        Desc:  %s" % (rec.desc)

        #if debug > 2:



# ------------------------------------------------------------
if __name__ == "__main__":
    # execute only if run as a script
    print("Being executed directly ......")
    main()

# ------------------------------------------------------------
''' Do not execute the following lines. Make it a comment.

--------------------------------------------------------------------------------
v 3.0
Major refactor in many areas

- The "state" field must be one of
  I - Incomplete
  C - Complete
  N - Will not be completed

- Added support for the 3.0 record type
- Refined the debug output. Has 4 levels
  0 - No debug
  1 - Brief debug output
  2 - Include more extensive tokens, fields
  3 - Include parse info for every input line
  
--------------------------------------------------------------------------------
v 2.2
- Added a little debug output. Minor change.

v 2.1
- Didn't record a change

v 2.0
- Fix logic for printing either Complete or Incomplete records.

v 2.0
- Add argparse() and process command line args.

v 1.1
- Add try around asssignments to catch IndexError. Helps catch malformed records.


'''

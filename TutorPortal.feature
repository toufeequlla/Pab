@sanity
Feature: Tutor Portal
Scenario Outline: verify right side pre class screen of tutor
    Given Open the '<tutorlPortalUrl>' Portal using Chrome
    And  login to tutor Portal
    When  click on 'Join Now' button
    And   Wait for 2 seconds
    And  validate 'bg video screen' is displayed
    And  Validate 'Start Class Mic' is displayed
    And  Validate 'start class cam' is displayed
    And  Validate 'setting' symbol is displayed
    And  Validate 'av_setting' is displayed
    And  Validate 'location' symbol is displayed
    And  Validate the 'centre name' having the '<centre_name>' is displayed
    And  Validate 'calendar' symbol is displayed
    And  Validate 'DateAndDay' that is current day is displayed
    And  Validate 'clock' symbol is displayed
    And  Validate the 'SessionTime' having the '<SessionTime>' is displayed
    And  Validate the 'Session plan' having 'Session' and 'Plan' is displayed
    And  Validate the 'Session Slides' having 'Session' and 'Slides' is displayed
    And  Validate the 'Class Log' having 'Class' and 'Log' is displayed
    And  Validate the 'Class Forum' having 'Class' and 'Forum' is displayed
    And  Validate the 'Student Details' having 'Student' and 'Details' is displayed
    And  Validate the 'Chapter Name' having the '<ChapterName>' is displayed
    And  Validate the 'Subject' having the '<Subject>' is displayed
    And  Validate the 'Syllabus' having the '<Syllabus>' is displayed
    And  Validate the 'Grade' having the '<Grade>' is displayed
    And  Validate the 'Chapter Name' having the '<ChapterName>' is displayed
    And  Validate the 'Subject' having the '<Subject>' is displayed
    And  Validate the 'Syllabus' having the '<Syllabus>' is displayed
    And  Validate the 'Grade' having the '<Grade>' is displayed
    And  Wait for 5 seconds

  Examples: TestData
   |tutorlPortalUrl | centre_name                    | SessionTime | ChapterName | Subject | Syllabus | Grade |
   |config:url>tutorPortalUrl  | config:CentreData>CentreName | config:SessionTimeData>SessionTime | config:SubjectDetails>ChapterName | config:SubjectDetails>Subject | config:SubjectDetails>Syllabus | config:SubjectDetails>Grade |

Scenario Outline: verify mic,cam,av setting action pre class screen of tutor
    Given Open the '<tutorlPortalUrl>' Portal using Chrome
    And login to tutor Portal
    When  click on 'Join Now' button
    And   Wait for 2 seconds
    Then  click on 'mic on' button and Validate 'mic off' button is displayed
    And   Wait for 2 seconds
    Then  click on 'mic off' button and Validate 'mic on' button is displayed
    And   Wait for 2 seconds
    Then  click on 'cam on' button and Validate 'cam off' button is displayed
    And   Wait for 2 seconds
    Then  click on 'cam off' button and Validate 'cam on' button is displayed
    And   Wait for 3 seconds
    Then  click on 'av setting' button
    And   Validate 'av setting text' is displayed
    And   Wait for 3 seconds


    Examples: TestData
        |tutorlPortalUrl |
        |config:url>tutorPortalUrl |


Scenario Outline: verify Preview on  pre class screen of tutor
    Given Open the '<tutorlPortalUrl>' Portal using Chrome
    And login to tutor Portal
    When  click on 'Join Now' button
    And   Wait for 2 seconds
    Then  click on the 'Session Slides' having 'Session' and 'Slides' is displayed
    And   click on 'Slide zoom icon' button for '<ImageSlide>'
    And   Validate 'Imag Slide' is displayed
    And   Wait for 5 seconds
    Then  click on 'Preview Close' button
    And   Wait for 5 seconds
    And  click on 'Slide zoom icon' button for '<VideoSlide>'
    And  Validate 'video slide' is displayed
    And  Wait for 5 seconds
    Then click on 'play and pause' button and Validate 'Pause video button' button is displayed
    And  Wait for 5 seconds
    Then click on 'play and pause' button and Validate 'Play video button' button is displayed
    And  Wait for 5 seconds
    Then click on 'video sound' button and Validate 'mute video' button is displayed
    And  Wait for 5 seconds
    Then click on 'mute video' button and Validate 'video sound' button is displayed
    And  Wait for 5 seconds


    Examples: TestData
   |tutorlPortalUrl  |  ImageSlide | VideoSlide |
   |config:url>tutorPortalUrl | config:SlideNo>ImageSlide | config:SlideNo>VideoSlide |

Scenario Outline: verify In class view  in class screen of tutor
    Given Open the '<tutorlPortalUrl>' Portal using Chrome
    And login to tutor Portal
    When  click on 'Join Now' button
    And   Wait for 2 seconds
    And   click on 'start class' button for 'Start Class'
    And   Validate the 'Global Control Text' having the 'Student global controls' is displayed
    Then Validate 'signal_strength' text is displayed
    And   Validate the 'end class' having the 'End Class' is displayed
    And   validate 'Timer' is displayed
    And   Wait for 2 seconds
    Then  Validate 'tutor card' is displayed
    Then  click on 'tutor card mic on' button and Validate 'tutor card mic off' button is displayed
    And   Wait for 3 seconds
    Then  click on 'tutor card mic off' button and Validate 'tutor card mic on' button is displayed
    And   Wait for 3 seconds
    Then  click on 'tutor card cam on' button and Validate 'tutor card cam off' button is displayed
    And   Wait for 3 seconds
    Then  click on 'tutor card cam off' button and Validate 'tutor card cam on' button is displayed
    And   Wait for 5 seconds

    Examples: TestData
        |tutorlPortalUrl |
        |config:url>tutorPortalUrl  |

Scenario Outline: verify Global Mic and cam in class screen of tutor
    Given Open the '<tutorlPortalUrl>' Portal using Chrome
    And login to tutor Portal
    When  click on 'Join Now' button
    And   Wait for 2 seconds
    And   click on 'start class' button for 'Start Class'
    Then click on 'Global student mic on' button
    And   Wait for 1 seconds
    Then click on 'Global student chat on' button
    Then Validate 'focus_mode_on' text is displayed
    And   Wait for 2 seconds
    Then click on 'Global student mic off' button
    And   Wait for 5 seconds
    Then click on 'Global student chat off' button
    And   Wait for 2 seconds
    Then click on 'Global student cam on' button and Validate 'Global student cam off' button is displayed
    And   Wait for 2 seconds
    Then click on 'Global student cam off' button and Validate 'Global student cam on' button is displayed
    And   Wait for 2 seconds
    Then click on 'Global student mic on' button and Validate 'Global student mic off' button is displayed
    And   Wait for 2 seconds
    Then click on 'Global student mic off' button and Validate 'Global student mic on' button is displayed
    And   Wait for 2 seconds
    Then click on 'Global student chat on' button and Validate 'Global student chat off' button is displayed
    And   Wait for 2 seconds
    Then click on 'Global student chat off' button and Validate 'Global student chat on' button is displayed
    And   Wait for 5 seconds


    Examples: TestData
     |tutorlPortalUrl |
     |config:url>tutorPortalUrl   |


#Scenario Outline: verify slide presentation in class screen of tutor
#    Given Open the '<tutorlPortalUrl>' Portal using Chrome
#    And login to tutor Portal
#    When  click on 'Join Now' button
#    And   Wait for 2 seconds
#    And   click on 'start class' button for 'Start Class'
#    Then click on the 'Session Slides' having 'Session' and 'Slides' is displayed
#    And  click on 'Session Presentation' button for '<ImageSlide>'
#    And  Wait for 5 seconds
#    And  click on 'Session Presentation' button for '<VideoSlide>'
#    And  Wait for 5 seconds
#    And  click on 'Session Presentation' button for '<PollSlide>'
#    And  Wait for 5 seconds
#    And  click on 'Session Presentation' button for '<gif>'
#
#    Examples: TestData
#    |tutorlPortalUrl |email                 | password             |  ImageSlide | VideoSlide | PollSlide | gif |
#    |config:url>tutorPortalUrl|config:login>username    | config:login>password |  config:SlideNo>ImageSlide | config:SlideNo>VideoSlide | config:SlideNo>PollSlide | config:SlideNo>gif |
#
Scenario Outline: verify add blank slide and  tool box in class of tutor
    Given Open the '<tutorlPortalUrl>' Portal using Chrome
    And   login to tutor Portal
    When  click on 'Join Now' button
    And   Wait for 2 seconds
    And   click on 'start class' button for 'Start Class'
    Then  click on the 'Session Slides' having 'Session' and 'Slides' is displayed
    Then  click on 'add_slide' button
    Then  click on 'blank slide presentation' button
    Then  click on 'Toggle Toolbox' button
    Then  Validate 'whiteboard_toolbox' is displayed
    Then  click on 'selector icon' button
    Then  click on 'pen icon' button
    Then  click on 'color icon' button
    Then  click on 'size icon' button
    Then  click on 'Laser pointer icon' button
    Then  click on 'shapes select' button
    Then  click on 'ellipse icon' button
    Then  click on 'polygon icon' button
    Then  click on 'star icon' button
    Then  click on 'line icon' button
    Then  click on 'Rectangle icon' button
    Then  click on 'Text icon' button
    Then  click on 'clear icon' button
    And   Wait for 2 seconds
    Then  click on 'Delete blank slide' button
    And   Wait for 5 seconds


    Examples: TestData
     |tutorlPortalUrl |
     |config:url>tutorPortalUrl|

##Scenario Outline: verify white board writting on blank slide
##    Given Open "link" Portal using Chrome
##    And   Enter email '<email>' and password '<password>' in Tutor portal
##    When  click on 'Join Now' button
##    And   Wait for 2 seconds
##    And   click on 'start class' button for 'Start Class'
##    And   Wait for 5 seconds
##    Then  click on the 'Session Slides' having 'Session' and 'Slides' is displayed
##    Then  click on 'add_slide' button
##    Then  click on 'blank slide presentation' button
##    Then  click on 'Toggle Toolbox' button
##    Then  click on 'Text icon' button
##    Then  write '<WhiteBoardText>' on 'whiteboard'
##    Then  Validate 'whiteboard text' having '<WhiteBoardText>' is displayed
##    And   Wait for 5 seconds
##    Then  Validate 'clear icon' functionality
##    And   Wait for 5 seconds
##    Then  click on 'Delete blank slide' button
##
##
#    Examples: TestData
#    |email                 | password             | WhiteBoardText |
#    |config:login>username    | config:login>password | BTC |
#
Scenario Outline: verify student details page
    Given Open the '<tutorlPortalUrl>' Portal using Chrome
    And   login to tutor Portal
    When  click on 'Join Now' button
    And   Wait for 2 seconds
    And   click on 'start class' button for 'Start Class'
    And   Wait for 5 seconds
    Then  click on the 'Student Details' having 'Student' and 'Details' is displayed
    And   Wait for 5 seconds
    Then  click on 'attendance tab' button for 'Attendance'
    Then  click on 'attendance' button for 'Present'
    And   Validate 'attendance name' is displayed
    And   Validate 'attendance attendance history' is displayed
    Then  click on 'attendance' button for 'Absent'
    And   Wait for 5 seconds
    And   Validate 'attendance name' is displayed
    And   Validate 'attendance attendance history' is displayed
    And   validate 'profile pic' is displayed
    And   validate the 'student name' having the '<studentName>' is displayed
    And   validate 'attended count' of '<studentName>' is displayed
    And   validate 'Total class' of '<studentName>' is displayed
    And   validate 'Attendance percentage' of '<studentName>' is displayed


    Examples: TestData
       |tutorlPortalUrl    | studentName |
      |config:url>tutorPortalUrl |config:StudentLogin>StudentName |
    @prod
    Scenario Outline: verify Tutor and Student detail flow
    Given Open the '<tutorlPortalUrl>' Portal using Chrome
    And login to tutor Portal
    When  click on 'Join Now' button
    And   Wait for 2 seconds
    And   click on 'start class' button for 'Start Class'
    Then click on the 'Session Slides' having 'Session' and 'Slides' is displayed
    And  open new tab with '<studentUrl>'
    And  Wait for 5 seconds
    And  Enter email '<StudentUsername>' and password '<StudentPassword>' in student portal with '<StudentUserId>'
    And  Wait for 5 seconds
    And  click on 'Student Join' button
    And  Wait for 5 seconds
    And  click on 'student join class' button
    And  Wait for 5 seconds
    And  switch to old window
    And  click on 'Session Presentation' button for '<ImageSlide>'
    And  Wait for 5 seconds
    And  New window opens
    And  validate 'image slide presented' is displayed
    And  click on 'handraise' button
    And  validate 'handraise icon' is displayed
    And  validate 'handraise text' is displayed
    And  switch to old window
    Then validate 'student card handraise' of '<StudentName>' is displayed
    And  Wait for 5 seconds
    And  New window opens
    And  click on 'handraise text' button
    And  Wait for 1 seconds
    And  validate 'handsdown toast message heading' is displayed
    And  validate 'handsdown toast message text' is displayed
    And  switch to old window
    And  Wait for 2 seconds
    Then click on 'Global student mic on' button
    Then click on 'Global student chat on' button
    Then Validate 'focus_mode_on' text is displayed
    And  New window opens
    And  validate 'focus mode toast title' is displayed
    And  validate 'focus mode toast subtitle' is displayed
    And  Validate 'focusmode icon' is displayed
    And  Validate 'student focusmode text' is displayed
    And  Validate 'presentation fullscreen' is displayed
    Then click on 'student mic off grey' button
    And  validate 'mic off grey icon' is displayed
    And  validate 'mic off toast message heading' is displayed
    And  validate 'mic off toast message text' is displayed
    And  Wait for 5 seconds
    Then click on 'student cam on' button
    And  validate 'cam on icon' is displayed
    And  validate 'cam on toast message' is displayed
    And  Wait for 5 seconds
    And  switch to old window
    Then click on 'add_slide' button
    Then click on 'blank slide presentation' button
    Then  click on 'Toggle Toolbox' button
    Then  click on 'Text icon' button
    And   Wait for 2 seconds
    Then  write '<WhiteBoardText>' on 'whiteboard'
    Then  Validate the 'whiteboard text' having the '<WhiteBoardText>' is displayed
    And  New window opens
    And  Wait for 15 seconds
    Then Validate the 'whiteboard text' having the '<WhiteBoardText>' is displayed
    And  switch to old window
    And  Wait for 2 seconds
    Then Validate 'clear icon' functionality
    Then click on 'Delete blank slide' button
    Then click on the 'Class Forum' having 'Class' and 'Forum' is displayed
    Then Enter '<TutorChat>' as text for 'tutor chat box'
    Then click on 'tutor chat send button' button
    And  Wait for 5 seconds
    And  New window opens
    And  Validate the 'tutor chat on student chat box' having the '<TutorChat>' is displayed
    And  Wait for 5 seconds
    Then Enter '<StudentChat>' as text for 'tutor chat box'
    Then click on 'tutor chat send button' button
    And  switch to old window
    And  Validate the 'student chat on tutor chat box' having '<StudentName>' and '<StudentChat>' is displayed
    Then click on the 'Session Slides' having 'Session' and 'Slides' is displayed
    And  click on 'Session Presentation' button for '<VideoSlide>'
    And  Wait for 5 seconds
    And  Validate 'Global student mic off' is displayed
    And  New window opens
    And  validate 'video slide presented' is displayed
    And  switch to old window
    And  Wait for 5 seconds
    And  click on 'Session Presentation' button for '<PollSlide>'
    And  Wait for 5 seconds
    And  New window opens
    And  validate 'poll slide presented' is displayed
    And  validate 'poll slde question' is displayed
    And  validate 'poll slide questionoption' is displayed
    And  validate 'poll_slide_option_header' is displayed
    And  Validate the 'poll slide option text' having the 'A' is displayed
    And  Validate the 'poll slide option text' having the 'B' is displayed
    And  Validate the 'poll slide option text' having the 'C' is displayed
    And  Validate the 'poll slide option text' having the 'D' is displayed
    And  validate 'poll left option' is displayed
    And  validate 'poll tutor card' is displayed
    And  validate 'poll student card' is displayed
    And  validate 'poll slide timer' is displayed
    And  Wait for 5 seconds
    And  switch to old window
    And  click on 'Session Presentation' button for '<gif>'
    And  Wait for 3 seconds
#    Then click on 'Global student mic off' button
#    Then click on 'Global student chat off' button
#    And  New window opens
#    Then click on 'individual student mic_off' button
#    And  switch to old window
#    And  mouseHover on 'student card' with '<StudentName>'
#    Then click on 'student card top right notification' button for '<StudentName>'
#    And  Wait for 5 seconds
#    Then click on 'turn off audio notification' button
#    And  New window opens
#    Then mouseHover on 'student mic off grey'
#    And  validate 'mic off grey icon' is displayed
#    And  validate 'mic off toast message heading' is displayed
#    And  validate 'mic off toast message text' is displayed
#    And  Wait for 5 seconds
#    And  switch to old window

    Examples: TestData
   | studentUrl |tutorlPortalUrl |  ImageSlide | VideoSlide | PollSlide | gif | TutorChat | StudentChat | StudentName |  WhiteBoardText | StudentUsername | StudentPassword | StudentUserId |
   | config:url>studentPortalUrl |  config:url>tutorPortalUrl   |  config:SlideNo>ImageSlide | config:SlideNo>VideoSlide | config:SlideNo>PollSlide | config:SlideNo>gif | TutorBTC | StudentBTC |  config:StudentLogin>StudentName |BTC| config:StudentLogin>StudentUsername | config:StudentLogin>StudentPassword | config:StudentLogin>StudentUserId |

#    Scenario Outline: verify Tutor and Student mic and cam functionality
#    Given Open the '<tutorlPortalUrl>' Portal using Chrome
#    And login to tutor Portal
#    When  click on 'Join Now' button
#    And   Wait for 2 seconds
#    And   click on 'start class' button for 'Start Class'
#    And Check mic before run
#    And Check cam before run
#    And Wait for 5 seconds
#    Then click on the 'Session Slides' having 'Session' and 'Slides' is displayed
#    And  open new tab with '<studentUrl>'
#    And  Wait for 5 seconds
#    And  Enter email '<StudentUsername>' and password '<StudentPassword>' in student portal with '<StudentUserId>'
#    And  Wait for 5 seconds
#    And  click on 'Student Join' button
#    And  Wait for 5 seconds
#    And  click on 'student join class' button
#    And  Wait for 5 seconds
#    And  switch to old window
#    And  click on 'Session Presentation' button for '<ImageSlide>'
#    And  mouseHover on 'student card' with '<StudentName>'
#    Then click on 'student card top right notification' button for '<StudentName>'
#    And click on 'reward close button' button
#    And  Wait for 5 seconds
#    Then click on 'turn off audio notification' button
#    And click on 'reward close button' button
#    And  New window opens
#    Then mouseHover on 'student mic off grey'
#    And  validate 'mic off grey icon' is displayed
#    And  validate 'mic off toast message heading' is displayed
#    And  validate 'mic off toast message text' is displayed
#    And  Wait for 5 seconds
#    And  switch to old window
#    Then click on 'Global student mic off' button
#    Then click on 'Global student chat off' button
#    And  New window opens
#    Then click on 'individual student mic_off' button
#    And  switch to old window

#    Examples:TestData
#    |studentUrl |tutorlPortalUrl |  ImageSlide | StudentName | StudentUsername | StudentPassword |
#    | config:url>studentPortalUrl |  config:url>tutorPortalUrl | config:SlideNo>ImageSlide| config:StudentLogin>StudentName | config:StudentLogin>StudentUsername | config:StudentLogin>StudentPassword |




# Screen-and-Keys-Detection

1. **Identification of Unauthorized Key Usage**: The primary goal is to detect and flag the use of _restricted or unauthorized keys_ (such as `ctrl+c`, `ctrl+v`, `ctrl+a`, `ctrl+x`, `ctrl+t`, `ctrl+w`, `alt+shift+tab`, `alt+tab`, `alt+esc`,` win+tab`, `ctrl+esc`, `ctrl+alt+delete`, `function` keys, and the `Window` key) on the computer keyboard during the exam. (in this case, System Run)

2. **Detection of Navigation Beyond the Test Interface**: The system is designed to monitor and identify any attempts by the student (user) to _switch or interact with other windows or applications_ while working within the test window interface (currently active IDE window) during the examination (System Run).

This implementation utilizes the `"Keyboard"` library for _Unauthorized Key Detection_ and the `"pygetwindow"` library for detecting _attempts to navigate away from the test interface_.


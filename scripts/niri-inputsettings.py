#!/usr/bin/env python3

import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QRadioButton, QLabel, QFrame,
                             QButtonGroup, QPushButton, QCheckBox, QDoubleSpinBox,
                             QComboBox, QTabWidget, QSpinBox, QLineEdit, QGroupBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


# Configuration path:
CONFIG_PATH = os.path.join(
    os.environ.get('XDG_CONFIG_HOME', os.path.expanduser('~/.config')),
    'lxqt', 'wayland', 'src', 'input.kdl'
)


class GeneralTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # General configuration section
        general_frame = QFrame()
        general_frame.setFrameStyle(QFrame.Shape.StyledPanel)
        general_layout = QVBoxLayout(general_frame)

        # General checkboxes
        self.warp_mouse_to_focus_checkbox = QCheckBox('Warp mouse to focus')
        self.focus_follows_mouse_checkbox = QCheckBox('Focus follows mouse')
        self.disable_power_key_checkbox = QCheckBox('Disable power key handling')
        self.workspace_auto_back_forth_checkbox = QCheckBox('Workspace auto back and forth')

        general_layout.addWidget(self.warp_mouse_to_focus_checkbox)
        general_layout.addWidget(self.focus_follows_mouse_checkbox)
        general_layout.addWidget(self.disable_power_key_checkbox)
        general_layout.addWidget(self.workspace_auto_back_forth_checkbox)

        # Mod key selection with radio buttons
        general_layout.addSpacing(10)  # Adds 10px of empty space
        mod_key_label = QLabel('Mod Key:')
        general_layout.addWidget(mod_key_label)

        self.mod_key_group = QButtonGroup(self)
        self.super_radio = QRadioButton('Super')
        self.alt_radio = QRadioButton('Alt')
        self.ctrl_radio = QRadioButton('Ctrl')

        self.mod_key_group.addButton(self.super_radio)
        self.mod_key_group.addButton(self.alt_radio)
        self.mod_key_group.addButton(self.ctrl_radio)

        # Default to Super
        self.super_radio.setChecked(True)

        # Layout for radio buttons
        mod_key_radio_layout = QHBoxLayout()
        mod_key_radio_layout.addWidget(self.super_radio)
        mod_key_radio_layout.addWidget(self.alt_radio)
        mod_key_radio_layout.addWidget(self.ctrl_radio)
        mod_key_radio_layout.addStretch()

        general_layout.addLayout(mod_key_radio_layout)

        layout.addWidget(general_frame)
        layout.addStretch()



class TouchpadTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Touchpad configuration section
        touchpad_frame = QFrame()
        touchpad_frame.setFrameStyle(QFrame.Shape.StyledPanel)
        touchpad_layout = QVBoxLayout(touchpad_frame)

        # Touchpad checkboxes
        self.tap_checkbox = QCheckBox('Tap to click')
        self.natural_scroll_checkbox = QCheckBox('Natural scroll')
        self.drag_lock_checkbox = QCheckBox('Drag lock')
        self.disable_external_mouse_checkbox = QCheckBox('Disable when external mouse connected')
        self.dwt_checkbox = QCheckBox('Disable while typing')
        self.left_handed_checkbox = QCheckBox('Left handed')

        touchpad_layout.addWidget(self.tap_checkbox)
        touchpad_layout.addWidget(self.natural_scroll_checkbox)
        touchpad_layout.addWidget(self.drag_lock_checkbox)
        touchpad_layout.addWidget(self.disable_external_mouse_checkbox)
        touchpad_layout.addWidget(self.dwt_checkbox)
        touchpad_layout.addWidget(self.left_handed_checkbox)

        # Scroll method selection
        touchpad_layout.addSpacing(10)  # Adds 10px of empty space
        scroll_label = QLabel('Scroll Method:')
        touchpad_layout.addWidget(scroll_label)

        self.scroll_group = QButtonGroup(self)
        self.two_finger_radio = QRadioButton('Two Finger')
        self.edge_radio = QRadioButton('Edge')

        self.scroll_group.addButton(self.two_finger_radio)
        self.scroll_group.addButton(self.edge_radio)

        touchpad_layout.addWidget(self.two_finger_radio)
        touchpad_layout.addWidget(self.edge_radio)

        # Acceleration speed
        accel_speed_layout = QHBoxLayout()
        accel_speed_label = QLabel('Acceleration Speed:')
        self.accel_speed_spinbox = QDoubleSpinBox()
        self.accel_speed_spinbox.setRange(0.0, 1.0)
        self.accel_speed_spinbox.setSingleStep(0.1)
        self.accel_speed_spinbox.setValue(0.2)
        self.accel_speed_spinbox.setDecimals(1)

        accel_speed_layout.addWidget(accel_speed_label)
        accel_speed_layout.addWidget(self.accel_speed_spinbox)
        accel_speed_layout.addStretch()
        touchpad_layout.addLayout(accel_speed_layout)

        # Acceleration profile
        accel_profile_layout = QHBoxLayout()
        accel_profile_label = QLabel('Acceleration Profile:')
        self.accel_profile_combobox = QComboBox()
        self.accel_profile_combobox.addItems(["flat", "adaptive"])

        accel_profile_layout.addWidget(accel_profile_label)
        accel_profile_layout.addWidget(self.accel_profile_combobox)
        accel_profile_layout.addStretch()
        touchpad_layout.addLayout(accel_profile_layout)

        layout.addWidget(touchpad_frame)
        layout.addStretch()


class MouseTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Mouse configuration section
        mouse_frame = QFrame()
        mouse_frame.setFrameStyle(QFrame.Shape.StyledPanel)
        mouse_layout = QVBoxLayout(mouse_frame)

        # Mouse checkboxes
        self.natural_scroll_checkbox = QCheckBox('Natural scroll')
        self.left_handed_checkbox = QCheckBox('Left handed')
        self.middle_emulation_checkbox = QCheckBox('Middle button emulation')

        mouse_layout.addWidget(self.natural_scroll_checkbox)
        mouse_layout.addWidget(self.left_handed_checkbox)
        mouse_layout.addWidget(self.middle_emulation_checkbox)

        # Acceleration speed
        accel_speed_layout = QHBoxLayout()
        accel_speed_label = QLabel('Acceleration Speed:')
        self.accel_speed_spinbox = QDoubleSpinBox()
        self.accel_speed_spinbox.setRange(0.0, 1.0)
        self.accel_speed_spinbox.setSingleStep(0.1)
        self.accel_speed_spinbox.setValue(0.2)
        self.accel_speed_spinbox.setDecimals(1)

        accel_speed_layout.addWidget(accel_speed_label)
        accel_speed_layout.addWidget(self.accel_speed_spinbox)
        accel_speed_layout.addStretch()
        mouse_layout.addLayout(accel_speed_layout)

        # Acceleration profile
        accel_profile_layout = QHBoxLayout()
        accel_profile_label = QLabel('Acceleration Profile:')
        self.accel_profile_combobox = QComboBox()
        self.accel_profile_combobox.addItems(["flat", "adaptive"])

        accel_profile_layout.addWidget(accel_profile_label)
        accel_profile_layout.addWidget(self.accel_profile_combobox)
        accel_profile_layout.addStretch()
        mouse_layout.addLayout(accel_profile_layout)

        # Scroll factor
        scroll_factor_layout = QHBoxLayout()
        scroll_factor_label = QLabel('Scroll Factor:')
        self.scroll_factor_spinbox = QDoubleSpinBox()
        self.scroll_factor_spinbox.setRange(0.1, 3.0)
        self.scroll_factor_spinbox.setSingleStep(0.1)
        self.scroll_factor_spinbox.setValue(1.0)
        self.scroll_factor_spinbox.setDecimals(1)

        scroll_factor_layout.addWidget(scroll_factor_label)
        scroll_factor_layout.addWidget(self.scroll_factor_spinbox)
        scroll_factor_layout.addStretch()
        mouse_layout.addLayout(scroll_factor_layout)

        layout.addWidget(mouse_frame)
        layout.addStretch()


class KeyboardTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # Keyboard configuration section
        keyboard_frame = QFrame()
        keyboard_frame.setFrameStyle(QFrame.Shape.StyledPanel)
        keyboard_layout = QVBoxLayout(keyboard_frame)

        # Numlock checkbox
        self.numlock_checkbox = QCheckBox('Num Lock enabled')
        keyboard_layout.addWidget(self.numlock_checkbox)

        # Track layout
        track_layout_layout = QHBoxLayout()
        track_layout_label = QLabel('Track Layout:')
        self.track_layout_combobox = QComboBox()
        self.track_layout_combobox.addItems(["window", "global"])

        track_layout_layout.addWidget(track_layout_label)
        track_layout_layout.addWidget(self.track_layout_combobox)
        track_layout_layout.addStretch()
        keyboard_layout.addLayout(track_layout_layout)

        # XKB Settings Group
        xkb_group = QGroupBox("XKB Settings")
        xkb_layout = QVBoxLayout(xkb_group)

        # Layout
        layout_layout = QHBoxLayout()
        layout_label = QLabel('Layout:')
        self.layout_edit = QLineEdit()
        self.layout_edit.setText("us")

        layout_layout.addWidget(layout_label)
        layout_layout.addWidget(self.layout_edit)
        layout_layout.addStretch()
        xkb_layout.addLayout(layout_layout)

        # Options
        options_layout = QHBoxLayout()
        options_label = QLabel('Options:')
        self.options_edit = QLineEdit()
        self.options_edit.setText("grp:alt_shift_toggle,compose:rctrl")

        options_layout.addWidget(options_label)
        options_layout.addWidget(self.options_edit)
        options_layout.addStretch()
        xkb_layout.addLayout(options_layout)

        keyboard_layout.addWidget(xkb_group)

        # Repeat settings
        repeat_group = QGroupBox("Repeat Settings")
        repeat_layout = QVBoxLayout(repeat_group)

        # Repeat delay
        repeat_delay_layout = QHBoxLayout()
        repeat_delay_label = QLabel('Repeat Delay:')
        self.repeat_delay_spinbox = QSpinBox()
        self.repeat_delay_spinbox.setRange(100, 2000)
        self.repeat_delay_spinbox.setSingleStep(100)
        self.repeat_delay_spinbox.setValue(500)
        self.repeat_delay_spinbox.setSuffix(' ms')

        repeat_delay_layout.addWidget(repeat_delay_label)
        repeat_delay_layout.addWidget(self.repeat_delay_spinbox)
        repeat_delay_layout.addStretch()
        repeat_layout.addLayout(repeat_delay_layout)

        # Repeat rate
        repeat_rate_layout = QHBoxLayout()
        repeat_rate_label = QLabel('Repeat Rate:')
        self.repeat_rate_spinbox = QSpinBox()
        self.repeat_rate_spinbox.setRange(1, 100)
        self.repeat_rate_spinbox.setValue(30)

        repeat_rate_layout.addWidget(repeat_rate_label)
        repeat_rate_layout.addWidget(self.repeat_rate_spinbox)
        repeat_rate_layout.addStretch()
        repeat_layout.addLayout(repeat_rate_layout)

        keyboard_layout.addWidget(repeat_group)

        layout.addWidget(keyboard_frame)
        layout.addStretch()


class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.load_settings()

    def init_ui(self):
        self.setWindowTitle('Niri Input Settings')
        self.setFixedSize(500, 550)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # Create tab widget
        self.tabs = QTabWidget()

        # Create tabs
        self.general_tab = GeneralTab(self)
        self.touchpad_tab = TouchpadTab(self)
        self.mouse_tab = MouseTab(self)
        self.keyboard_tab = KeyboardTab(self)

        # Add tabs to tab widget
        self.tabs.addTab(self.general_tab, "General")
        self.tabs.addTab(self.touchpad_tab, "Touchpad")
        self.tabs.addTab(self.mouse_tab, "Mouse")
        self.tabs.addTab(self.keyboard_tab, "Keyboard")

        main_layout.addWidget(self.tabs)

        # Button layout
        button_layout = QHBoxLayout()

        # Apply button
        apply_btn = QPushButton('Apply')

        apply_btn.setFixedWidth(100)
        apply_btn.clicked.connect(self.apply_settings)

        # Close button
        close_btn = QPushButton('Close')
        close_btn.setFixedWidth(100)
        close_btn.clicked.connect(self.close)
        button_layout.addStretch()  # This will push buttons to the right
        button_layout.addWidget(apply_btn)
        button_layout.addWidget(close_btn)

        main_layout.addLayout(button_layout)

    def get_config_path(self):
        """Get the configuration file path"""
        # Ensure the directory exists
        config_dir = os.path.dirname(CONFIG_PATH)
        os.makedirs(config_dir, exist_ok=True)
        return CONFIG_PATH

    def apply_settings(self):
        """Save settings to input.kdl in KDL format"""
        config_path = self.get_config_path()
        self.save_general_config(config_path)
        self.save_touchpad_config(config_path)
        self.save_mouse_config(config_path)
        self.save_keyboard_config(config_path)
        print(f"Settings applied to {config_path}!")

    def save_general_config(self, config_path):
        """Save general configuration to input.kdl in KDL format"""
        try:
            with open(config_path, 'w') as f:
                f.write('// Generated by niri-inputsettings.py \n')
                f.write('input {\n')
                f.write('    \n')

                # Write general settings
                if self.general_tab.warp_mouse_to_focus_checkbox.isChecked():
                    f.write('    warp-mouse-to-focus\n')
                else:
                    f.write('    // warp-mouse-to-focus\n')

                if self.general_tab.focus_follows_mouse_checkbox.isChecked():
                    f.write('    focus-follows-mouse\n')
                else:
                    f.write('    // focus-follows-mouse\n')
                # Write disable power key handling
                if self.general_tab.disable_power_key_checkbox.isChecked():
                    f.write('    disable-power-key-handling\n')
                else:
                    f.write('    // disable-power-key-handling\n')

                # Write workspace auto back and forth
                if self.general_tab.workspace_auto_back_forth_checkbox.isChecked():
                    f.write('    workspace-auto-back-and-forth\n')
                else:
                    f.write('    // workspace-auto-back-and-forth\n')

                # Write mod key based on radio button selection
                if self.general_tab.super_radio.isChecked():
                    f.write('    mod-key "Super"\n')
                elif self.general_tab.alt_radio.isChecked():
                    f.write('    mod-key "Alt"\n')
                elif self.general_tab.ctrl_radio.isChecked():
                    f.write('    mod-key "Ctrl"\n')

        except Exception as e:
            print(f"Error saving general configuration: {e}")

    def save_touchpad_config(self, config_path):
        """Save touchpad configuration to input.kdl in KDL format"""
        try:
            with open(config_path, 'a') as f:  # Append to the file
                f.write('    \n')
                f.write('    touchpad {\n')

                # Write tap setting
                if self.touchpad_tab.tap_checkbox.isChecked():
                    f.write('        tap\n')
                else:
                    f.write('        // tap\n')

                # Write dwt setting
                if self.touchpad_tab.dwt_checkbox.isChecked():
                    f.write('        dwt\n')
                else:
                    f.write('        // dwt\n')

                # Write natural scroll setting
                if self.touchpad_tab.natural_scroll_checkbox.isChecked():
                    f.write('        natural-scroll\n')
                else:
                    f.write('        // natural-scroll\n')

                # Write drag lock setting
                if self.touchpad_tab.drag_lock_checkbox.isChecked():
                    f.write('        drag-lock\n')
                else:
                    f.write('        // drag-lock\n')

                # Write disabled on external mouse setting
                if self.touchpad_tab.disable_external_mouse_checkbox.isChecked():
                    f.write('        disabled-on-external-mouse\n')
                else:
                    f.write('        // disabled-on-external-mouse\n')

                # Write left-handed setting
                if self.touchpad_tab.left_handed_checkbox.isChecked():
                    f.write('        left-handed\n')
                else:
                    f.write('        // left-handed\n')

                # Write scroll method
                if self.touchpad_tab.two_finger_radio.isChecked():
                    f.write('        scroll-method "two-finger"\n')
                elif self.touchpad_tab.edge_radio.isChecked():
                    f.write('        scroll-method "edge"\n')
                else:
                    f.write('        // scroll-method "two-finger"\n')

                # Always write acceleration speed
                f.write(f'        accel-speed {self.touchpad_tab.accel_speed_spinbox.value()}\n')

                # Always write acceleration profile
                f.write(f'        accel-profile "{self.touchpad_tab.accel_profile_combobox.currentText()}"\n')

                f.write('    }\n')

        except Exception as e:
            print(f"Error saving touchpad configuration: {e}")

    def save_mouse_config(self, config_path):
        """Save mouse configuration to input.kdl in KDL format"""
        try:
            with open(config_path, 'a') as f:  # Append to the file
                f.write('    \n')
                f.write('    mouse {\n')

                # Write natural scroll setting
                if self.mouse_tab.natural_scroll_checkbox.isChecked():
                    f.write('        natural-scroll\n')
                else:
                    f.write('        // natural-scroll\n')

                # Write left-handed setting
                if self.mouse_tab.left_handed_checkbox.isChecked():
                    f.write('        left-handed\n')
                else:
                    f.write('        // left-handed\n')

                # Write middle emulation setting
                if self.mouse_tab.middle_emulation_checkbox.isChecked():
                    f.write('        middle-emulation\n')
                else:
                    f.write('        // middle-emulation\n')

                # Always write acceleration settings
                f.write(f'        accel-speed {self.mouse_tab.accel_speed_spinbox.value()}\n')
                f.write(f'        accel-profile "{self.mouse_tab.accel_profile_combobox.currentText()}"\n')
                f.write(f'        scroll-factor {self.mouse_tab.scroll_factor_spinbox.value()}\n')

                f.write('    }\n')

        except Exception as e:
            print(f"Error saving mouse configuration: {e}")

    def save_keyboard_config(self, config_path):
        """Save keyboard configuration to input.kdl in KDL format"""
        try:
            with open(config_path, 'a') as f:  # Append to the file
                f.write('    \n')
                f.write('    keyboard {\n')
                f.write(f'        track-layout "{self.keyboard_tab.track_layout_combobox.currentText()}"\n')

                # Write numlock setting
                if self.keyboard_tab.numlock_checkbox.isChecked():
                    f.write('        numlock\n')
                else:
                    f.write('        // numlock\n')

                # Write xkb block
                f.write('        xkb {\n')
                f.write(f'           layout "{self.keyboard_tab.layout_edit.text()}"\n')
                f.write(f'           options "{self.keyboard_tab.options_edit.text()}"\n')
                f.write('           //options "grp:alt_shift_toggle"\n')
                f.write('        }\n')

                # Write repeat settings
                f.write(f'        repeat-delay {self.keyboard_tab.repeat_delay_spinbox.value()}\n')
                f.write(f'        repeat-rate {self.keyboard_tab.repeat_rate_spinbox.value()}\n')

                f.write('    }\n')
                f.write('}\n')

        except Exception as e:
            print(f"Error saving keyboard configuration: {e}")

    def load_settings(self):
        import re  # Add this line here
        """Load existing settings from input.kdl"""
        try:
            config_path = self.get_config_path()
            with open(config_path, 'r') as f:
                content = f.read()

                # Parse general settings
                if 'warp-mouse-to-focus' in content and '// warp-mouse-to-focus' not in content:
                    self.general_tab.warp_mouse_to_focus_checkbox.setChecked(True)

                if 'focus-follows-mouse' in content and '// focus-follows-mouse' not in content:
                    self.general_tab.focus_follows_mouse_checkbox.setChecked(True)
               # Parse disable power key handling
                if 'disable-power-key-handling' in content and '// disable-power-key-handling' not in content:
                    self.general_tab.disable_power_key_checkbox.setChecked(True)

                # Parse workspace auto back and forth
                if 'workspace-auto-back-and-forth' in content and '// workspace-auto-back-and-forth' not in content:
                    self.general_tab.workspace_auto_back_forth_checkbox.setChecked(True)

                # Parse mod key
                match = re.search(r'mod-key\s+"([^"]+)"', content)
                if match:
                    mod_key = match.group(1)
                    if mod_key == "Super":
                        self.general_tab.super_radio.setChecked(True)
                    elif mod_key == "Alt":
                        self.general_tab.alt_radio.setChecked(True)
                    elif mod_key == "Ctrl":
                        self.general_tab.ctrl_radio.setChecked(True)

                # Parse touchpad settings
                if 'tap' in content and '// tap' not in content:
                    self.touchpad_tab.tap_checkbox.setChecked(True)

                if 'dwt' in content and '// dwt' not in content:
                    self.touchpad_tab.dwt_checkbox.setChecked(True)

                if 'natural-scroll' in content and '// natural-scroll' not in content:
                    self.touchpad_tab.natural_scroll_checkbox.setChecked(True)

                if 'drag-lock' in content and '// drag-lock' not in content:
                    self.touchpad_tab.drag_lock_checkbox.setChecked(True)

                if 'disabled-on-external-mouse' in content and '// disabled-on-external-mouse' not in content:
                    self.touchpad_tab.disable_external_mouse_checkbox.setChecked(True)

                if 'left-handed' in content and '// left-handed' not in content:
                    self.touchpad_tab.left_handed_checkbox.setChecked(True)

                if 'scroll-method "two-finger"' in content and '// scroll-method "two-finger"' not in content:
                    self.touchpad_tab.two_finger_radio.setChecked(True)
                elif 'scroll-method "edge"' in content and '// scroll-method "edge"' not in content:
                    self.touchpad_tab.edge_radio.setChecked(True)
                else:
                    self.touchpad_tab.two_finger_radio.setChecked(True)

                import re
                match = re.search(r'accel-speed\s+([\d.]+)', content)
                if match:
                    self.touchpad_tab.accel_speed_spinbox.setValue(float(match.group(1)))

                match = re.search(r'accel-profile\s+"([^"]+)"', content)
                if match:
                    profile = match.group(1)
                    index = self.touchpad_tab.accel_profile_combobox.findText(profile)
                    if index >= 0:
                        self.touchpad_tab.accel_profile_combobox.setCurrentIndex(index)

                # Parse mouse settings
                if 'natural-scroll' in content and '// natural-scroll' not in content:
                    self.mouse_tab.natural_scroll_checkbox.setChecked(True)

                if 'left-handed' in content and '// left-handed' not in content:
                    self.mouse_tab.left_handed_checkbox.setChecked(True)

                if 'middle-emulation' in content and '// middle-emulation' not in content:
                    self.mouse_tab.middle_emulation_checkbox.setChecked(True)

                match = re.search(r'accel-speed\s+([\d.]+)', content)
                if match:
                    self.mouse_tab.accel_speed_spinbox.setValue(float(match.group(1)))

                match = re.search(r'accel-profile\s+"([^"]+)"', content)
                if match:
                    profile = match.group(1)
                    index = self.mouse_tab.accel_profile_combobox.findText(profile)
                    if index >= 0:
                        self.mouse_tab.accel_profile_combobox.setCurrentIndex(index)

                match = re.search(r'scroll-factor\s+([\d.]+)', content)
                if match:
                    self.mouse_tab.scroll_factor_spinbox.setValue(float(match.group(1)))

                # Parse keyboard settings
                match = re.search(r'track-layout\s+"([^"]+)"', content)
                if match:
                    track_layout = match.group(1)
                    index = self.keyboard_tab.track_layout_combobox.findText(track_layout)
                    if index >= 0:
                        self.keyboard_tab.track_layout_combobox.setCurrentIndex(index)

                if 'numlock' in content and '// numlock' not in content:
                    self.keyboard_tab.numlock_checkbox.setChecked(True)

                # Look for layout inside xkb block
                xkb_match = re.search(r'xkb\s*{.*?layout\s+"([^"]+)"', content, re.DOTALL)
                if xkb_match:
                    self.keyboard_tab.layout_edit.setText(xkb_match.group(1))

                # Look for options inside xkb block
                options_match = re.search(r'xkb\s*{.*?options\s+"([^"]+)"', content, re.DOTALL)
                if options_match:
                    self.keyboard_tab.options_edit.setText(options_match.group(1))

                match = re.search(r'repeat-delay\s+(\d+)', content)
                if match:
                    self.keyboard_tab.repeat_delay_spinbox.setValue(int(match.group(1)))

                match = re.search(r'repeat-rate\s+(\d+)', content)
                if match:
                    self.keyboard_tab.repeat_rate_spinbox.setValue(int(match.group(1)))

        except FileNotFoundError:
            # If file doesn't exist, use defaults
            self.touchpad_tab.tap_checkbox.setChecked(True)
            self.touchpad_tab.natural_scroll_checkbox.setChecked(True)
            self.touchpad_tab.two_finger_radio.setChecked(True)
            print(f"No existing config file found at {self.get_config_path()}, using defaults")
        except Exception as e:
            print(f"Error loading configuration: {e}")


def main():
    app = QApplication(sys.argv)

    # Set application properties
    app.setApplicationName('Niri Input Settings')
    app.setApplicationVersion('0.1')

    window = SettingsWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()

# FormatVerilog for Sublime Text (Sublime Text Verilog 格式化插件)

一个简单的 Sublime Text 3/4 插件，用于在Ctrl+S保存时使用 [`verible-verilog-format`](https://github.com/chipsalliance/verible) 自动格式化 Verilog 文件。

## 功能特性 (Features)

*   保存时 (`Ctrl+S`) 自动格式化 Verilog 代码。
*   使用 `verible-verilog-format` 可执行文件。
*   可通过配置启用或禁用。
*   可配置 `verible-verilog-format` 可执行文件的路径。

## 安装 (Installation)

1.  前往 Sublime Text 的 `Packages` 目录 (Preferences -> Browse Packages...)。
2.  创建一个名为 `FormatVerilog` 的新文件夹。
3.  将插件文件 (`format_verilog.py`, `FormatVerilog.sublime-settings`, `README.md`, `Main.sublime-menu`) 和 `verible` 可执行文件（或其所在目录）放入此文件夹。例如，将 `verible-verilog-format.exe` 放在 `Packages/FormatVerilog/verible/` 下。
4.  重启 Sublime Text。

## 配置 (Configuration)

通过设置文件进行配置：`Packages/FormatVerilog/FormatVerilog.sublime-settings` (Preferences -> Package Settings -> FormatVerilog -> Settings)。

*   `enabled`: 设置为 `true` 以启用保存时格式化，`false` 则禁用。默认为 `true`。
*   `verible_executable_path`: **必需**。设置 `verible-verilog-format.exe` 的**完整路径**，或者如果将可执行文件放在插件目录下的 `verible` 子目录中，请使用相对路径 `${packages}/FormatVerilog/verible/verible-verilog-format.exe`。**即使在 Windows 上，路径分隔符也请使用正斜杠 `/`**。
*   **Verible 格式化选项 (取消注释以覆盖默认值):**
    *   `verible_indentation_spaces`: 每个缩进级别的空格数 (默认: `2`)
    *   `verible_wrap_spaces`: 换行后的额外缩进空格数 (默认: `4`)
    *   `verible_column_limit`: 代码行的最大列数限制 (默认: `100`)
    *   `verible_wrap_end_else_clauses`: 如果为 `true`，则将 `end` 和 `else` 分开放在不同行 (默认: `false`)
    *   `verible_try_wrap_long_lines`: 尝试优化长行的换行 (实验性) (默认: `false`)
    *   `verible_line_break_penalty`: 换行的计算权重 (默认: `2`)
    *   `verible_over_column_limit_penalty`: 超过列限制的计算权重 (默认: `1000`)
    *   `verible_assignment_statement_alignment`: 赋值语句对齐方式 (`align`, `flush-left`, `preserve`, `infer`) (默认: `infer`)
    *   `verible_case_items_alignment`: case 项对齐方式 (默认: `infer`)
    *   `verible_class_member_variable_alignment`: 类成员变量对齐方式 (默认: `infer`)
    *   `verible_distribution_items_alignment`: distribution 项对齐方式 (默认: `infer`)
    *   `verible_enum_assignment_statement_alignment`: enum 赋值语句对齐方式 (默认: `infer`)
    *   `verible_formal_parameters_alignment`: 形式参数对齐方式 (默认: `infer`)
    *   `verible_formal_parameters_indentation`: 形式参数缩进方式 (`indent`, `wrap`) (默认: `wrap`)
    *   `verible_module_net_variable_alignment`: 模块网络/变量对齐方式 (默认: `infer`)
    *   `verible_named_parameter_alignment`: 命名参数对齐方式 (默认: `infer`)
    *   `verible_named_parameter_indentation`: 命名参数缩进方式 (`indent`, `wrap`) (默认: `wrap`)
    *   `verible_named_port_alignment`: 命名端口对齐方式 (默认: `infer`)
    *   `verible_named_port_indentation`: 命名端口缩进方式 (`indent`, `wrap`) (默认: `wrap`)
    *   `verible_port_declarations_alignment`: 端口声明对齐方式 (默认: `infer`)
    *   `verible_port_declarations_indentation`: 端口声明缩进方式 (`indent`, `wrap`) (默认: `wrap`)
    *   `verible_port_declarations_right_align_packed_dimensions`: 端口声明中 packed 维度右对齐 (默认: `false`)
    *   `verible_port_declarations_right_align_unpacked_dimensions`: 端口声明中 unpacked 维度右对齐 (默认: `false`)
    *   `verible_struct_union_members_alignment`: 结构体/联合体成员对齐方式 (默认: `infer`)
    *   `verible_compact_indexing_and_selections`: 紧凑索引/位选择 (默认: `true`)
    *   `verible_expand_coverpoints`: 总是展开 coverpoints (默认: `false`)
    *   `verible_show_equally_optimal_wrappings`: 显示等效最优换行 (调试用) (默认: `false`)

    示例 (如果放在插件的 `verible` 子目录中):
    ```json
    {
      "enabled": true,
      "verible_executable_path": "${packages}/FormatVerilog/verible/verible-verilog-format.exe"
    }
    ```

## 使用方法 (Usage)

1.  确保在设置中正确配置了 `verible_executable_path`。
2.  确保 `enabled` 设置为 `true`。
3.  打开一个 Verilog 文件 (确保语法设置为 Verilog)。
4.  保存文件 (`Ctrl+S`)。代码应自动格式化。

如果格式化失败，请检查 Sublime Text 控制台 (`View > Show Console`) 中的错误信息。








---

**(English Version Below)**

# FormatVerilog for Sublime Text

A simple Sublime Text 3/4 plugin to automatically format Verilog files using [`verible-verilog-format`](https://github.com/chipsalliance/verible) on save.

## Features

*   Automatically formats Verilog code upon saving (`Ctrl+S`).
*   Uses the `verible-verilog-format` executable.
*   Configurable enable/disable switch.
*   Configurable path to the `verible-verilog-format` executable.

## Installation

1.  Go to your Sublime Text `Packages` directory (Preferences -> Browse Packages...).
2.  Create a new folder named `FormatVerilog`.
3.  Place the plugin files (`format_verilog.py`, `FormatVerilog.sublime-settings`, `README.md`, `Main.sublime-menu`) and the `verible` executable (or its directory) inside this folder. For example, place `verible-verilog-format.exe` under `Packages/FormatVerilog/verible/`.
4.  Restart Sublime Text.

## Configuration

Configuration is done via the settings file: `Packages/FormatVerilog/FormatVerilog.sublime-settings` (Preferences -> Package Settings -> FormatVerilog -> Settings).

*   `enabled`: Set to `true` to enable format on save, `false` to disable. Defaults to `true`.
*   `verible_executable_path`: **Required**. Set the *full path* to your `verible-verilog-format.exe`, or use the relative path `${packages}/FormatVerilog/verible/verible-verilog-format.exe` if you place the executable inside the `verible` subdirectory of the plugin. **Use forward slashes (`/`) for the path, even on Windows.**
*   **Verible Formatting Options (Uncomment to override defaults):**
    *   `verible_indentation_spaces`: Spaces per indentation level (Default: `2`)
    *   `verible_wrap_spaces`: Extra spaces for wrapped lines (Default: `4`)
    *   `verible_column_limit`: Max column limit for lines (Default: `100`)
    *   `verible_wrap_end_else_clauses`: Place `end` and `else` on separate lines (Default: `false`)
    *   `verible_try_wrap_long_lines`: Try to wrap long lines (Experimental) (Default: `false`)
    *   `verible_line_break_penalty`: Penalty for line breaks (Default: `2`)
    *   `verible_over_column_limit_penalty`: Penalty for exceeding column limit (Default: `1000`)
    *   `verible_assignment_statement_alignment`: Alignment for assignments (`align`, `flush-left`, `preserve`, `infer`) (Default: `infer`)
    *   `verible_case_items_alignment`: Alignment for case items (Default: `infer`)
    *   `verible_class_member_variable_alignment`: Alignment for class members (Default: `infer`)
    *   `verible_distribution_items_alignment`: Alignment for distribution items (Default: `infer`)
    *   `verible_enum_assignment_statement_alignment`: Alignment for enum assignments (Default: `infer`)
    *   `verible_formal_parameters_alignment`: Alignment for formal parameters (Default: `infer`)
    *   `verible_formal_parameters_indentation`: Indentation for formal parameters (`indent`, `wrap`) (Default: `wrap`)
    *   `verible_module_net_variable_alignment`: Alignment for module nets/vars (Default: `infer`)
    *   `verible_named_parameter_alignment`: Alignment for named parameters (Default: `infer`)
    *   `verible_named_parameter_indentation`: Indentation for named parameters (`indent`, `wrap`) (Default: `wrap`)
    *   `verible_named_port_alignment`: Alignment for named ports (Default: `infer`)
    *   `verible_named_port_indentation`: Indentation for named ports (`indent`, `wrap`) (Default: `wrap`)
    *   `verible_port_declarations_alignment`: Alignment for port declarations (Default: `infer`)
    *   `verible_port_declarations_indentation`: Indentation for port declarations (`indent`, `wrap`) (Default: `wrap`)
    *   `verible_port_declarations_right_align_packed_dimensions`: Right-align packed dimensions in ports (Default: `false`)
    *   `verible_port_declarations_right_align_unpacked_dimensions`: Right-align unpacked dimensions in ports (Default: `false`)
    *   `verible_struct_union_members_alignment`: Alignment for struct/union members (Default: `infer`)
    *   `verible_compact_indexing_and_selections`: Compact indexing/slicing (Default: `true`)
    *   `verible_expand_coverpoints`: Always expand coverpoints (Default: `false`)
    *   `verible_show_equally_optimal_wrappings`: Show equally optimal wrappings (Debug) (Default: `false`)

    Example (if placed in `verible` subdirectory):
    ```json
    {
      "enabled": true,
      "verible_executable_path": "${packages}/FormatVerilog/verible/verible-verilog-format.exe"
    }
    ```

## Usage

1.  Ensure `verible_executable_path` is correctly set in the settings.
2.  Make sure `enabled` is `true`.
3.  Open a Verilog file (ensure the syntax is set to Verilog).
4.  Save the file (`Ctrl+S`). The code should be automatically formatted.

Check the Sublime Text console (`View > Show Console`) for any error messages if formatting fails. 
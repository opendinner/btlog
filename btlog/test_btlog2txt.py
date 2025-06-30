import unittest
import os
import json
from btlog2txt import input_file, output_file  # 导入目标模块

class TestBtlog2txt(unittest.TestCase):
    def test_output_file_exists(self):
        # 假设主程序已运行，验证输出文件存在
        self.assertTrue(os.path.exists(output_file))

    def test_json_content(self):
        # 验证 JSON 文件可读
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.assertIn('actions', data)

if __name__ == '__main__':
    unittest.main()
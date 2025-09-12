import unittest
import sys
import io
from unittest import mock
from pathlib import Path

# 动态添加 battlelog 目录到系统路径
sys.path.append(str(Path(__file__).parent.parent))
import log_parser


class TestLogParser(unittest.TestCase):
    def setUp(self):
        """设置通用测试数据和 mock mapping"""
        # Mock mapping模块
        self.skill_patch = mock.patch.dict('log_parser.m.skill_mapping', {
            101: '火球术',
            102: '冰霜新星'
        })
        self.effect_patch = mock.patch.dict('log_parser.m.effect_mapping', {
            201: '燃烧',
            202: '冻结'
        })
        self.skill_patch.start()
        self.effect_patch.start()

        # 公共测试数据
        self.attack_data = [12345, {'unitId': 1, 'skillId': 101}]
        self.defend_data = [12345, {'unitId': -1, 'skillId': 101}]
    
    def tearDown(self):
        """清理 mock"""
        self.skill_patch.stop()
        self.effect_patch.stop()
    
    def capture_output(self, func, *args):
        """捕获函数输出的上下文管理器"""
        with io.StringIO() as buf:
            sys.stdout = buf
            func(*args)
            sys.stdout = sys.__stdout__
            return buf.getvalue()
    
    def test_recognize_camp(self):
        """测试阵营识别"""
        positive_data = [0, {'unitId': 100}]
        negative_data = [0, {'unitId': -100}]
        
        self.assertEqual(log_parser.recognize_camp(positive_data), '左边')
        self.assertEqual(log_parser.recognize_camp(negative_data), '右边')
    
    # def test_parse_state_add(self):
    #     """测试状态添加解析"""
    #     data = [12345, {
    #         'unitId': 1,
    #         'effectId': 201,
    #         'isAdd': 1
    #     }]
        
    #     output = self.capture_output(log_parser.parse_state, data)
    #     self.assertIn('添加了效果 燃烧', output)
    #     self.assertIn('攻击方', output)
    
    # def test_parse_state_remove(self):
    #     """测试状态移除解析"""
    #     data = [12345, {
    #         'unitId': -1,
    #         'effectId': 202,
    #         'isAdd': 0
    #     }]
        
    #     output = self.capture_output(log_parser.parse_state, data)
    #     self.assertIn('移除了效果 冻结', output)
    #     self.assertIn('防守方', output)
    
    # def test_parse_action_basic(self):
    #     """测试基础技能输出"""
    #     output = self.capture_output(log_parser.parse_action, self.attack_data)
    #     self.assertIn('火球术', output)
    #     self.assertIn('攻击方', output)
    
    # def test_parse_action_critical(self):
    #     """测试暴击输出"""
    #     data = [12345, {
    #         'unitId': 1,
    #         'skillId': 101,
    #         'effect': [{
    #             'fighterId': 2,
    #             'damageMap': 100,
    #             'bCritical': True
    #         }]
    #     }]
        
    #     output = self.capture_output(log_parser.parse_action, data)
    #     self.assertIn('暴击!!! 100', output)
    
    # #def test_parse_action_evade(self):
    #     """测试闪避输出"""
    #     data = [12345, {
    #         'unitId': -1,
    #         'skillId': 102,
    #         'effect': [{
    #             'fighterId': -2,
    #             'bEvade': True
    #         }]
    #     }]
        
    #     output = self.capture_output(log_parser.parse_action, data)
    #     self.assertIn('闪避了攻击', output)
    #     self.assertIn('冻结', output)
    
    def test_parse_buffs_trigger(self):
        """测试 Buff 触发输出"""
        data =         [33,{
            "timestamp": 33,
            "unitId": 3,
            "effect": [
                {
                    "fighterId": -1,
                    "damageMap": {
                        "3": 10
                    },
                    "curHp": 241201
                }
            ]
        }]
        
        output = self.capture_output(log_parser.parse_buffs, data)
        self.assertIn(" 33 时, 右边的-1触发buff伤害 {'3': 10}，-1 当前血量为 241201，\n\n", output)
        self.assertIn('33', output)
    
    # def test_parse_dispatch(self):
    #     """测试 parse 函数分发逻辑"""
    #     # 测试 skillId 分支
    #     action_data = self.attack_data[1].copy()
    #     action_data.update({
    #         'skillId': 101,
    #         'effect': [{'damageMap': 100}]
    #     })
    #     test_data = [12345, action_data]
        
    #     output = self.capture_output(log_parser.parse, test_data)
    #     self.assertIn('火球术', output)
    #     self.assertIn('100', output)
        
    #     # 测试 effectId 分支
    #     state_data = {
    #         'unitId': -1,
    #         'effectId': 201,
    #         'isAdd': 1
    #     }
    #     test_data = [12345, state_data]
        
    #     output = self.capture_output(log_parser.parse, test_data)
    #     self.assertIn('燃烧', output)
    
    # def test_invalid_data(self):
        """测试无效数据处理"""
        # 测试无 effectId/skillId 的数据
        invalid_data = [12345, {'unitId': 1}]
        output = self.capture_output(log_parser.parse, invalid_data)
        self.assertEqual(output, '')  # 应该不抛出异常且无输出

if __name__ == '__main__':
    unittest.main()
import re

css = """

<div class="mana_dashboard" style="wdith:100%; height:100%">
	<div class="head">
		<h1>大数据可视化通用素材</h1>
	</div>
	<div class="mainbox">
		<ul class="clearfix">
			<li>
				<div class="boxall" style="height:calc(33.3333% - .25rem)">
					<div class="tit01">模块标题</div>
					<div class="boxnav nav01 mana_chart line_chart" template="block1"></div>
					<div class="boxfoot"></div>
				</div>
				<div style="height:calc(33.3333% - .25rem); margin-bottom: .25rem;">
					<div class="boxall" style="height: 100%; width:calc(50% - .08rem); float: left;">
						<div class="tit01">模块标题</div>
						<div class="boxnav nav01 mana_chart radar_chart" template="block2" ></div>
						<div class="boxfoot"></div>
					</div>
					<div class="boxall qweb_template" template="block3" style="height: 100%; width:calc(50% - .08rem); float: right;">
					</div>
				</div>
				<div class="boxall" style="height:calc(33.3333% - .25rem)">
					<div class="tit01">模块标题</div>
					<div class="boxnav nav01 mana_chart line_chart" template="block4"></div>
					<div class="boxfoot"></div>
				</div>
			</li>
			<li>
				<div class="boxall" style="height:calc(33.33333% - .25rem)">
					<div class="tit02">本月计划</div>
					<div class="boxnav nav02 qweb_template">
						<div>
							<p class="p1">完成/计划</p>
							<p class="p2"><span class="counter">15633</span>/<span class="counter">68000</span></p>
							<p class="p3">
								<span><i class="dot dot1"></i>未完成：52367</span>
								<span><i class="dot dot2"></i>完成率：22.9%</span>
							</p>
						</div>
					</div>
					<div class="boxfoot"></div>
				</div>
				<div class="boxall qweb_template" template="table1" style="height:calc(66.666666% - .25rem)" tempalte="block5">
				</div>
			</li>
			<li>
				<div class="boxall qweb_template" template="table2" style="height:calc(100% - .25rem); padding: 0;">
				</div>
			</li>
		</ul>
	</div>
</div>
"""

font_size_one = 95.75
font_size_two = 13
scale = font_size_one / font_size_two

# 定义正则表达式匹配规则
pattern = r'(\d*\.?\d+)rem'

# 定义替换函数
def repl(match):
    value = float(match.group(1)) * scale
    return f'{value:.2}rem'

# 执行替换操作
new_style = re.sub(pattern, repl, css)

# 输出结果
print(new_style)
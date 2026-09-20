<template>
	<view class="detail-page">
		<scroll-view class="scroll-container" scroll-y="true">
			<!-- 招财图鉴主图 -->
			<image class="detail-img" src="/static/招财图鉴.png" mode="widthFix"></image>

			<!-- 底部兑奖规则发光对话框卡片（向上上移） -->
			<view class="rules-card">
				<view class="rules-header">
					<text class="rules-title">兑换规则</text>
				</view>
				<view class="rules-content">
					<text class="rule-item">① 集齐指定卡片后，可解锁对应奖励。</text>
					<text class="rule-item">② 「西财神 + 南财神」可兑换 <text class="highlight-gold">￥588现金奖励</text>。</text>
					<text class="rule-item">③ 「东财神 + 西财神 + 南财神 + 北财神」集齐后，可兑换 <text class="highlight-gold">￥888现金奖励</text>。</text>
					<text class="rule-item">④ 每套奖励的兑换条件及领取方式，以活动页面实际规则为准。</text>
				</view>
			</view>

			<!-- 底部安全垫高区，防止内容被底部导航栏遮挡 -->
			<view class="bottom-safe-space"></view>
		</scroll-view>

		<!-- 底部导航栏组件 -->
		<NeonTabBar :current="3" />
	</view>
</template>

<script>
import NeonTabBar from '@/components/NeonTabBar.uvue';

export default {
	components: {
		NeonTabBar
	}
};
</script>

<style>
.detail-page {
	flex: 1;
	background-color: #030616;
	position: relative;
}
.scroll-container {
	flex: 1;
	width: 100%;
}
.detail-img {
	width: 100%;
	display: block;
	margin-top: 0;
}

/* 兑奖规则卡片：向上移动 */
.rules-card {
	margin-top: -28px; /* 负边距实现向上移动，贴紧图片内容 */
	margin-left: 16px;
	margin-right: 16px;
	padding-top: 14px;
	padding-bottom: 14px;
	padding-left: 16px;
	padding-right: 16px;
	border-radius: 14px;
	background-color: rgba(11, 17, 43, 0.85);
	backdrop-filter: blur(10px);
	border-width: 1px;
	border-style: solid;
	border-color: rgba(168, 85, 247, 0.6);
	box-shadow: 0 0 15px rgba(168, 85, 247, 0.25), inset 0 0 10px rgba(56, 189, 248, 0.1);
	flex-direction: column;
	position: relative;
	z-index: 5;
}

.rules-header {
	flex-direction: row;
	align-items: center;
	margin-bottom: 10px;
}

.rules-title {
	font-size: 15px;
	font-weight: bold;
	color: #ffffff;
	letter-spacing: 1px;
}

.rules-content {
	flex-direction: column;
}

.rule-item {
	font-size: 12px;
	color: #94a3b8;
	line-height: 20px;
	margin-bottom: 6px;
}

.rule-item:last-child {
	margin-bottom: 0;
}

.highlight-gold {
	color: #f59e0b;
	font-weight: bold;
}

.bottom-safe-space {
	height: 90px;
}
</style>

<template>
	<view class="detail-page">
		<scroll-view class="scroll-container" scroll-y="true">
			<image class="detail-img" src="/static/神兽图鉴.png" mode="widthFix"></image>
			<!-- 底部安全垫高区，防止内容被底部导航栏遮挡 -->
			<view class="bottom-safe-space"></view>
		</scroll-view>
		<view class="back-btn" @click="goBack">
			<text class="back-arrow">‹</text>
		</view>

		<!-- 底部导航栏组件 -->
		<NeonTabBar :current="3" />
	</view>
</template>

<script>
import NeonTabBar from '@/components/NeonTabBar.uvue';

export default {
	components: {
		NeonTabBar
	},
	methods: {
		goBack() {
			uni.navigateBack({
				fail() {
					uni.switchTab({ url: '/pages/card/card' });
				}
			});
		}
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
}
.back-btn {
	position: absolute;
	top: 40px;
	left: 16px;
	width: 36px;
	height: 36px;
	border-radius: 18px;
	background-color: rgba(0, 0, 0, 0.5);
	justify-content: center;
	align-items: center;
	z-index: 10;
}
.back-arrow {
	color: #ffffff;
	font-size: 24px;
	margin-top: -2px;
}
.bottom-safe-space {
	height: 80px;
}
</style>

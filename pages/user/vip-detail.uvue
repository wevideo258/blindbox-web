<template>
	<view class="detail-page">
		<scroll-view class="scroll-container" scroll-y="true">
			<!-- 年度会员详情长图 -->
			<image class="detail-img" src="/static/年度会员详情页.png" mode="widthFix"></image>
		</scroll-view>

		<!-- 顶部返回按钮 -->
		<view class="back-btn" @click="goBack">
			<text class="back-arrow">‹</text>
		</view>

		<!-- 底部 TabBar 组件 -->
		<NeonTabBar :current="4" />
	</view>
</template>

<script setup lang="uts">
import NeonTabBar from '@/components/NeonTabBar.uvue';

const goBack = () => {
	uni.navigateBack({
		fail() {
			uni.switchTab({ url: '/pages/user/user' });
		}
	});
};
</script>

<style>
.detail-page {
	flex: 1;
	width: 100%;
	height: 100%;
	background-color: #030616;
	position: relative;
}

.scroll-container {
	flex: 1;
	width: 100%;
	/* 留出底部 TabBar 的高度空间，避免遮挡底部长图内容 */
	padding-bottom: 70px;
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
	z-index: 99;
}

.back-arrow {
	color: #ffffff;
	font-size: 24px;
	margin-top: -2px;
}
</style>

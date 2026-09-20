<template>
	<scroll-view class="container" scroll-y="true">
		<!-- 顶部赛博背景图 -->
		<view class="top-bg-container">
			<image class="top-bg-img" src="/static/user背景.png" mode="aspectFill"></image>
			<!-- 底部渐变遮罩 -->
			<view class="top-bg-mask"></view>
		</view>

		<view class="top-header-area">
			<!-- 1. 顶栏 Header -->
			<view class="nav-bar">
				<view class="nav-left" @click="goBack">
					<text class="back-arrow">‹</text>
					<text class="nav-title">个人中心</text>
				</view>
				<view class="nav-right">
					<view class="icon-btn" @click="onCalendar">
						<text class="nav-icon">📅</text>
					</view>
					<view class="icon-btn" @click="onSettings">
						<text class="nav-icon">⚙️</text>
					</view>
				</view>
			</view>

			<!-- 2. 用户信息头部 -->
			<view class="user-profile-section">
				<view class="avatar-wrap">
					<image class="avatar-img" src="/static/用户头像.png" mode="aspectFill"></image>
				</view>

				<view class="user-info">
					<view class="name-row">
						<text class="user-name">ShiJieBok</text>
						<!-- 蓝色圆底✓认证标识 -->
						<view class="verify-badge">
							<text class="verify-check">✓</text>
						</view>
					</view>
					<text class="user-id">ID: 12345678</text>
					<view class="v2-tag">
						<image class="v2-icon-img" src="/static/V2.png" mode="aspectFit"></image>
						<text class="v2-text">V2</text>
					</view>
				</view>

				<view class="slogan-box">
					<text class="slogan-main">More Than</text>
					<text class="slogan-sub">A Figure</text>
					<text class="slogan-brand">SBebox</text>
				</view>
			</view>
		</view>

		<view class="content-body">
			<!-- 3. 会员等级/经验进度卡片（向上稍作移动） -->
			<view class="vip-level-card">
				<image class="vip-card-bg" src="/static/会员对话框背景.png" mode="scaleToFill"></image>

				<view class="level-badge-box">
					<image class="level-v2-img" src="/static/V2.png" mode="aspectFit"></image>
				</view>
				<view class="level-info">
					<view class="level-header">
						<text class="level-title">👑 青铜会员</text>
						<text class="arrow-icon">›</text>
					</view>
					<view class="desc-row">
						<text class="level-desc">当前 <text class="highlight-white">99/99</text> 经验 · 距离 V3 还差 <text class="highlight-white">1,900</text> 经验</text>
					</view>

					<!-- 进度条 -->
					<view class="progress-row">
						<view class="progress-bar-container">
							<view class="progress-fill" style="width: 99%;"></view>
						</view>
						<text class="progress-percent">99%</text>
					</view>
				</view>
			</view>

			<!-- 4. 资产/积分/卡片 3 列 Grid -->
			<view class="assets-grid">
				<!-- 左列：提现余额 -->
				<view class="asset-card asset-card-glow-purple">
					<view class="card-head">
						<text class="head-icon purple-bg">💳</text>
						<text class="head-title">提现余额</text>
					</view>
					<view class="amount-row">
						<text class="amount-symbol">¥</text>
						<text class="amount-val">88.50</text>
						<text class="amount-arrow">›</text>
					</view>
					<text class="sub-info">满 100元可提现</text>
					<view class="notice-time">
						<text class="time-icon">🕒</text>
						<text class="time-text">距离周三提现开启还剩 2天</text>
					</view>
				</view>

				<!-- 中列：商城积分 -->
				<view class="asset-card asset-card-glow-blue">
					<view class="card-head">
						<text class="head-icon blue-bg">💎</text>
						<text class="head-title">商城积分</text>
					</view>
					<view class="amount-row">
						<text class="amount-val">198.0</text>
						<text class="amount-arrow">›</text>
					</view>

					<view class="action-btn-group">
						<view class="asset-btn blue-btn" @click="onExchange">
							<text class="asset-btn-text">兑换余额</text>
						</view>
						<view class="asset-btn purple-btn" @click="onGoMall">
							<text class="asset-btn-text">去商城消费</text>
						</view>
					</view>
				</view>

				<!-- 右列：我的卡片 -->
				<view class="asset-card asset-card-glow-blue">
					<view class="card-head">
						<text class="head-icon blue-card-bg">🃏</text>
						<text class="head-title">我的卡片</text>
					</view>
					<view class="amount-row">
						<text class="amount-val">12</text>
						<text class="amount-unit">张</text>
						<text class="amount-arrow">›</text>
					</view>

					<view class="action-btn-group">
						<view class="asset-btn blue-btn" @click="onGoCard">
							<text class="asset-btn-text">去集卡</text>
						</view>
						<view class="asset-btn purple-btn" @click="onCardMarket">
							<text class="asset-btn-text">卡片集市</text>
						</view>
					</view>
				</view>
			</view>

			<!-- 5. 黄金开通会员 Banner -->
			<view class="vip-upgrade-banner" @click="onBuyVip">
				<image class="gold-badge-img" src="/static/年度会员.png" mode="aspectFit"></image>
				<view class="banner-text-box">
					<text class="banner-title">开通 ¥298 年会员</text>
					<text class="banner-sub">享15%佣金 / 双倍经验</text>
				</view>
				<view class="gold-arrow-btn">
					<text class="arrow-text">›</text>
				</view>
			</view>

			<!-- 6. 社区代理入口 Banner -->
			<view class="agent-banner" @click="onAgentApply">
				<image class="agent-badge-img" src="/static/代理.png" mode="aspectFit"></image>
				<view class="agent-text-box">
					<text class="agent-title">申请 ¥2,998 社区代理</text>
					<text class="agent-sub">团队收益 · 平台分红 · 更多权益</text>
				</view>
				<text class="agent-arrow">›</text>
			</view>

			<!-- 7. 我的订单区 -->
			<view class="order-section">
				<view class="section-head">
					<text class="section-title">我的订单</text>
					<view class="see-all-box" @click="onViewAllOrders">
						<text class="see-all">查看全部</text>
						<text class="head-arrow">›</text>
					</view>
				</view>

				<view class="order-grid">
					<view class="order-item" @click="onOrderType('待发货')">
						<view class="icon-wrap">
							<text class="order-icon">📦</text>
							<view class="badge-dot"><text class="badge-num">2</text></view>
						</view>
						<text class="order-label">待发货</text>
					</view>

					<view class="order-item" @click="onOrderType('待收货')">
						<view class="icon-wrap">
							<text class="order-icon">🚚</text>
						</view>
						<text class="order-label">待收货</text>
					</view>

					<view class="order-item" @click="onOrderType('已完成')">
						<view class="icon-wrap">
							<text class="order-icon">📋</text>
						</view>
						<text class="order-label">已完成</text>
					</view>

					<view class="order-item" @click="onOrderType('售后')">
						<view class="icon-wrap">
							<text class="order-icon">🎧</text>
						</view>
						<text class="order-label">售后</text>
					</view>
				</view>
			</view>

			<!-- 8. 功能菜单列表 -->
			<view class="menu-list">
				<view class="menu-item" @click="onMenuClick('我的经验值')">
					<view class="menu-left">
						<text class="menu-icon">✪</text>
						<text class="menu-name">我的经验值</text>
					</view>
					<view class="menu-right">
						<text class="menu-sub">成长记录</text>
						<text class="menu-arrow">›</text>
					</view>
				</view>

				<view class="menu-item border-top" @click="onMenuClick('我的任务')">
					<view class="menu-left">
						<text class="menu-icon">📋</text>
						<text class="menu-name">我的任务</text>
					</view>
					<view class="menu-right">
						<text class="menu-sub">去完成</text>
						<text class="menu-arrow">›</text>
					</view>
				</view>

				<view class="menu-item border-top" @click="onMenuClick('邀请好友')">
					<view class="menu-left">
						<text class="menu-icon">👥</text>
						<text class="menu-name">邀请好友</text>
					</view>
					<view class="menu-right">
						<text class="menu-sub">邀请赚奖励</text>
						<text class="menu-arrow">›</text>
					</view>
				</view>
			</view>
		</view>

		<!-- 底部 TabBar 组件 -->
		<NeonTabBar :current="4" />
	</scroll-view>
</template>

<script setup lang="uts">
import NeonTabBar from '@/components/NeonTabBar.uvue';

const goBack = () => {
	uni.navigateBack();
};

const onCalendar = () => {
	uni.showToast({ title: '打开日历', icon: 'none' });
};

const onSettings = () => {
	uni.showToast({ title: '打开设置', icon: 'none' });
};

const onExchange = () => {
	uni.showToast({ title: '兑换余额', icon: 'none' });
};

const onGoMall = () => {
	uni.switchTab({ url: '/pages/mall/mall' });
};

const onGoCard = () => {
	uni.switchTab({ url: '/pages/card/card' });
};

const onCardMarket = () => {
	uni.showToast({ title: '打开卡片集市', icon: 'none' });
};

// 【已修改】跳转到年度会员详情页
const onBuyVip = () => {
	uni.navigateTo({
		url: '/pages/user/vip-detail'
	});
};

const onAgentApply = () => {
	uni.showToast({ title: '申请社区代理', icon: 'none' });
};

const onViewAllOrders = () => {
	uni.showToast({ title: '查看全部订单', icon: 'none' });
};

const onOrderType = (type: string) => {
	uni.showToast({ title: `查看【${type}】`, icon: 'none' });
};

const onMenuClick = (title: string) => {
	uni.showToast({ title: `打开【${title}】`, icon: 'none' });
};
</script>

<style>
/* 样式保留不变 */
.container {
	flex: 1;
	background-color: #030616;
	position: relative;
}

.top-bg-container {
	position: absolute;
	left: 0;
	right: 0;
	top: 0;
	height: 190px;
	z-index: 0;
}

.top-bg-img {
	width: 100%;
	height: 100%;
}

.top-bg-mask {
	position: absolute;
	left: 0;
	right: 0;
	bottom: 0;
	height: 50px;
	background: linear-gradient(to bottom, rgba(3, 6, 22, 0) 0%, #030616 100%);
}

.top-header-area {
	position: relative;
	z-index: 1;
	padding-left: 10px;
	padding-right: 10px;
}

.nav-bar {
	flex-direction: row;
	justify-content: space-between;
	align-items: center;
	padding-top: 20px;
	padding-bottom: 8px;
	padding-left: 2px;
	padding-right: 2px;
}

.nav-left {
	flex-direction: row;
	align-items: center;
}

.back-arrow {
	font-size: 22px;
	color: #ffffff;
	margin-right: 4px;
}

.nav-title {
	font-size: 15px;
	font-weight: bold;
	color: #ffffff;
}

.nav-right {
	flex-direction: row;
	align-items: center;
}

.icon-btn {
	margin-left: 12px;
}

.nav-icon {
	font-size: 16px;
}

.content-body {
	position: relative;
	z-index: 1;
	padding-left: 10px;
	padding-right: 10px;
	padding-bottom: 110px;
}

.user-profile-section {
	flex-direction: row;
	align-items: center;
	padding-top: 8px;
	padding-bottom: 4px;
	position: relative;
}

.avatar-wrap {
	width: 72px;
	height: 72px;
	border-radius: 36px;
	border-width: 2px;
	border-style: solid;
	border-color: #a855f7;
	padding: 2px;
	background-color: rgba(3, 6, 22, 0.3);
}

.avatar-img {
	width: 100%;
	height: 100%;
	border-radius: 34px;
}

.user-info {
	margin-left: 12px;
	flex-direction: column;
}

.name-row {
	flex-direction: row;
	align-items: center;
}

.user-name {
	font-size: 16px;
	font-weight: bold;
	color: #ffffff;
}

.verify-badge {
	width: 14px;
	height: 14px;
	border-radius: 7px;
	background-color: #0095f6;
	align-items: center;
	justify-content: center;
	margin-left: 5px;
}

.verify-check {
	font-size: 9px;
	color: #ffffff;
	font-weight: bold;
	line-height: 14px;
	text-align: center;
}

.user-id {
	font-size: 10px;
	color: #cbd5e1;
	margin-top: 2px;
}

.v2-tag {
	background-color: rgba(254, 240, 138, 0.9);
	border-radius: 10px;
	padding-left: 6px;
	padding-right: 8px;
	padding-top: 2px;
	padding-bottom: 2px;
	margin-top: 5px;
	align-self: flex-start;
	flex-direction: row;
	align-items: center;
}

.v2-icon-img {
	width: 12px;
	height: 12px;
	margin-right: 3px;
}

.v2-text {
	font-size: 9px;
	color: #713f12;
	font-weight: bold;
}

.slogan-box {
	position: absolute;
	right: 0;
	top: 8px;
	flex-direction: column;
	align-items: flex-end;
}

.slogan-main {
	font-size: 13px;
	font-weight: 900;
	color: #38bdf8;
	font-style: italic;
}

.slogan-sub {
	font-size: 12px;
	font-weight: bold;
	color: #818cf8;
	font-style: italic;
}

.slogan-brand {
	font-size: 8px;
	color: #38bdf8;
}

.vip-level-card {
	position: relative;
	overflow: hidden;
	border-radius: 12px;
	padding-top: 18px;
	padding-bottom: 20px;
	padding-left: 14px;
	padding-right: 14px;
	min-height: 105px;
	flex-direction: row;
	align-items: center;
	margin-top: -8px;
	margin-bottom: 2px;
	background-color: transparent;
}

.vip-card-bg {
	position: absolute;
	left: 0;
	right: 0;
	top: 0;
	bottom: 0;
	width: 100%;
	height: 100%;
	z-index: 0;
}

.level-badge-box {
	position: relative;
	z-index: 1;
	margin-right: 12px;
	justify-content: center;
	align-items: center;
}

.level-v2-img {
	width: 58px;
	height: 58px;
}

.level-info {
	position: relative;
	z-index: 1;
	flex: 1;
	flex-direction: column;
}

.level-header {
	flex-direction: row;
	align-items: center;
}

.level-title {
	font-size: 13px;
	font-weight: bold;
	color: #ffffff;
}

.arrow-icon {
	font-size: 11px;
	color: #94a3b8;
	margin-left: 4px;
}

.desc-row {
	margin-top: 4px;
	margin-bottom: 8px;
}

.level-desc {
	font-size: 9px;
	color: #c7d2fe;
	line-height: 13px;
}

.highlight-white {
	color: #ffffff;
	font-weight: bold;
}

.progress-row {
	flex-direction: row;
	align-items: center;
	margin-top: 2px;
}

.progress-bar-container {
	flex: 1;
	height: 6px;
	background-color: rgba(15, 23, 42, 0.6);
	border-radius: 3px;
	overflow: hidden;
}

.progress-fill {
	height: 100%;
	background: linear-gradient(90deg, #38bdf8 0%, #818cf8 100%);
	border-radius: 3px;
}

.progress-percent {
	font-size: 9px;
	color: #ffffff;
	margin-left: 8px;
	font-weight: bold;
}

.assets-grid {
	flex-direction: row;
	justify-content: space-between;
	margin-top: -2px;
	margin-bottom: 12px;
	position: relative;
	z-index: 2;
}

.asset-card {
	width: 32%;
	background-color: rgba(11, 17, 43, 0.9);
	border-radius: 12px;
	padding: 8px;
	flex-direction: column;
}

.asset-card-glow-purple {
	border-width: 1px;
	border-style: solid;
	border-color: rgba(168, 85, 247, 0.6);
	box-shadow: 0 0 10px rgba(168, 85, 247, 0.35);
}

.asset-card-glow-blue {
	border-width: 1px;
	border-style: solid;
	border-color: rgba(56, 189, 248, 0.6);
	box-shadow: 0 0 10px rgba(56, 189, 248, 0.35);
}

.card-head {
	flex-direction: row;
	align-items: center;
}

.head-icon {
	font-size: 9px;
	padding: 2px;
	border-radius: 4px;
	margin-right: 3px;
}

.purple-bg { background-color: rgba(168, 85, 247, 0.2); }
.blue-bg { background-color: rgba(56, 189, 248, 0.2); }
.blue-card-bg { background-color: rgba(99, 102, 241, 0.2); }

.head-title {
	font-size: 9px;
	color: #94a3b8;
}

.amount-row {
	flex-direction: row;
	align-items: baseline;
	margin-top: 6px;
}

.amount-symbol {
	font-size: 10px;
	font-weight: bold;
	color: #fbbf24;
}

.amount-val {
	font-size: 15px;
	font-weight: 900;
	color: #fbbf24;
}

.amount-unit {
	font-size: 8px;
	color: #ffffff;
	margin-left: 2px;
}

.amount-arrow {
	font-size: 10px;
	color: #64748b;
	margin-left: 2px;
}

.sub-info {
	font-size: 7px;
	color: #64748b;
	margin-top: 4px;
}

.notice-time {
	flex-direction: row;
	align-items: center;
	margin-top: 6px;
}

.time-icon {
	font-size: 7px;
	margin-right: 2px;
}

.time-text {
	font-size: 6px;
	color: #94a3b8;
}

.action-btn-group {
	margin-top: 8px;
	flex-direction: column;
}

.asset-btn {
	height: 20px;
	border-radius: 10px;
	align-items: center;
	justify-content: center;
	margin-bottom: 4px;
}

.blue-btn { background-color: #3b82f6; }
.purple-btn { background-color: #8b5cf6; }

.asset-btn-text {
	font-size: 8px;
	color: #ffffff;
	font-weight: bold;
}

.vip-upgrade-banner {
	background: linear-gradient(90deg, #f59e0b 0%, #fbbf24 100%);
	border-radius: 12px;
	padding: 8px 12px;
	flex-direction: row;
	align-items: center;
	justify-content: space-between;
	margin-bottom: 10px;
}

.gold-badge-img {
	width: 60px;
	height: 60px;
}

.banner-text-box {
	flex: 1;
	flex-direction: column;
	margin-left: 10px;
}

.banner-title {
	font-size: 13px;
	font-weight: 900;
	color: #451a03;
}

.banner-sub {
	font-size: 9px;
	color: #78350f;
	margin-top: 2px;
}

.gold-arrow-btn {
	width: 24px;
	height: 24px;
	border-radius: 12px;
	background-color: #fef3c7;
	align-items: center;
	justify-content: center;
}

.arrow-text {
	font-size: 13px;
	color: #451a03;
	font-weight: bold;
}

.agent-banner {
	background: linear-gradient(90deg, #1e1b4b 0%, #311b92 100%);
	border-radius: 12px;
	border-width: 1px;
	border-style: solid;
	border-color: #6366f1;
	padding: 8px 12px;
	flex-direction: row;
	align-items: center;
	justify-content: space-between;
	margin-bottom: 10px;
}

.agent-badge-img {
	width: 60px;
	height: 60px;
}

.agent-text-box {
	flex: 1;
	flex-direction: column;
	margin-left: 10px;
}

.agent-title {
	font-size: 11px;
	font-weight: bold;
	color: #ffffff;
}

.agent-sub {
	font-size: 8px;
	color: #818cf8;
	margin-top: 2px;
}

.agent-arrow {
	font-size: 14px;
	color: #818cf8;
}

.order-section {
	background-color: rgba(11, 17, 43, 0.85);
	border-radius: 12px;
	border-width: 1px;
	border-style: solid;
	border-color: #1e293b;
	padding: 10px 12px;
	margin-bottom: 10px;
}

.section-head {
	flex-direction: row;
	justify-content: space-between;
	align-items: center;
	padding-bottom: 8px;
	border-bottom-width: 1px;
	border-bottom-style: solid;
	border-bottom-color: #1e293b;
}

.section-title {
	font-size: 11px;
	font-weight: bold;
	color: #ffffff;
}

.see-all-box {
	flex-direction: row;
	align-items: center;
}

.see-all {
	font-size: 8px;
	color: #64748b;
}

.head-arrow {
	font-size: 10px;
	color: #64748b;
	margin-left: 2px;
}

.order-grid {
	flex-direction: row;
	justify-content: space-around;
	padding-top: 10px;
}

.order-item {
	flex-direction: column;
	align-items: center;
}

.icon-wrap {
	position: relative;
}

.order-icon {
	font-size: 18px;
}

.badge-dot {
	position: absolute;
	top: -4px;
	right: -6px;
	background-color: #ef4444;
	border-radius: 6px;
	padding-left: 3px;
	padding-right: 3px;
}

.badge-num {
	font-size: 7px;
	color: #ffffff;
	font-weight: bold;
}

.order-label {
	font-size: 8px;
	color: #94a3b8;
	margin-top: 4px;
}

.menu-list {
	background-color: rgba(11, 17, 43, 0.85);
	border-radius: 12px;
	border-width: 1px;
	border-style: solid;
	border-color: #1e293b;
	padding-left: 12px;
	padding-right: 12px;
}

.menu-item {
	height: 38px;
	flex-direction: row;
	justify-content: space-between;
	align-items: center;
}

.border-top {
	border-top-width: 1px;
	border-top-style: solid;
	border-top-color: #1e293b;
}

.menu-left {
	flex-direction: row;
	align-items: center;
}

.menu-icon {
	font-size: 12px;
	margin-right: 8px;
}

.menu-name {
	font-size: 10px;
	color: #ffffff;
}

.menu-right {
	flex-direction: row;
	align-items: center;
}

.menu-sub {
	font-size: 8px;
	color: #64748b;
	margin-right: 4px;
}

.menu-arrow {
	font-size: 10px;
	color: #64748b;
}
</style>

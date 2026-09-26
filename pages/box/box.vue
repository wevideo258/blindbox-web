<template>
	<view class="page-container">
		<!-- 主内容滚动区 -->
		<scroll-view class="container" scroll-y="true">
			<!-- 1. 盲盒主区域：包裹背景图及所有覆盖元素 -->
			<view class="hero-stage-full">
				<!-- 背景盲盒大图 -->
				<image class="box-bg-full-img" src="/static/盲盒.png" mode="widthFix"></image>

				<!-- 覆盖在图片最顶部的 Header -->
				<view class="nav-header">
					<text class="back-btn" @click="handleBack">‹</text>
					<view class="placeholder-box"></view>
				</view>

				<!-- 覆盖在图片上半部的发光对话框标语 -->
				<view class="slogan-box">
					<text class="slogan-header-title">盲盒开启</text>
					<text class="slogan-main">请选择你心仪 <text class="highlight-purple">目标大奖</text></text>
					<text class="slogan-sub">选中后，开始抽奖后的中奖机率更大！</text>
				</view>

				<!-- 悬浮在图片两侧的左右切换箭头 -->
				<view class="arrow-btn left-arrow" @click="prevItem">
					<text class="arrow-icon">‹</text>
				</view>
				<view class="arrow-btn right-arrow" @click="nextItem">
					<text class="arrow-icon">›</text>
				</view>

				<!-- 覆盖在图片底部的商品标签卡片 -->
				<view class="prize-tag-card">
					<text class="prize-tag-title">{{ currentSelectedPrize.fullName }}</text>
					<view class="hot-badge">
						<text class="fire-icon">🔥</text>
						<text class="hot-text">当前最热门大奖</text>
					</view>
				</view>
			</view>

			<!-- 2. 下方内容区域 -->
			<view class="content-body">
				<!-- 4 个展示大奖卡片 (已按要求更新图片路径并移除底部热门标签) -->
				<view class="prize-select-section">
					<view class="prize-grid-wrapper">
						<view
							v-for="(item, index) in displayPrizeList"
							:key="index"
							class="prize-item-card"
							:class="{ 'prize-item-active': selectedPrizeIndex === index }"
							@click="selectPrize(index)"
						>
							<view class="prize-img-box">
								<image class="prize-img" :src="item.image" mode="aspectFit"></image>
							</view>
							<text class="prize-name">{{ item.name }}</text>
						</view>
					</view>
				</view>

				<!-- 本期盲盒与抽奖按钮区域 -->
				<view class="draw-action-card">
					<view class="card-top-info">
						<view class="info-left">
							<text class="box-title">拾界·9.9盲盒</text>
							<view class="info-meta">
								<view class="meta-item">
									<text class="meta-icon">🎁</text>
									<text class="meta-label">单价</text>
									<text class="meta-price">¥9.9</text>
									<text class="meta-unit">/ 次</text>
								</view>
								<view class="meta-item margin-l">
									<text class="meta-icon">💎</text>
									<text class="meta-label">官方正品</text>
									<text class="meta-guarantee">保障</text>
								</view>
							</view>
						</view>

						<view class="remain-badge">
							<text class="remain-text">本期剩余 <text class="remain-num">{{ remainingStock }}</text> 次</text>
						</view>
					</view>

					<!-- 渐变开启大按钮：触发真实后端抽奖请求 -->
					<view class="draw-btn" @click="startDraw">
						<text class="draw-btn-text">¥9.9 开启盲盒 ›</text>
					</view>

					<!-- 底部保障提示 -->
					<text class="guarantee-tips">抽中直接发货  ·  未抽中100%返还等额余额可提现</text>
				</view>

				<!-- 底部防 TabBar 遮挡的安全占位层 -->
				<view class="bottom-safe-space"></view>
			</view>
		</scroll-view>

		<!-- 3. 固定在底部的导航栏（TabBar） -->
		<view class="custom-tabbar">
			<view
				v-for="(tab, index) in tabList"
				:key="index"
				class="tabbar-item"
				:class="{ 'tabbar-item-active': activeTab === tab.id }"
				@click="switchTab(tab)"
			>
				<text class="tabbar-icon">{{ tab.icon }}</text>
				<text class="tabbar-label">{{ tab.name }}</text>
			</view>
		</view>

		<!-- 4. 后端抽奖结果展示弹窗 -->
		<view v-if="showResultModal" class="result-modal-mask">
			<view class="result-modal-content">
				<text class="modal-title">🎉 恭喜获得</text>
				<view class="prize-display-list">
					<view v-for="(item, index) in drawnPrizes" :key="index" class="prize-result-item">
						<text class="prize-type-badge">{{ item.rarity || item.type || '卡片' }}</text>
						<text class="prize-result-name">{{ item.name }}</text>
					</view>
				</view>
				<view class="modal-confirm-btn" @click="closeModal">
					<text class="confirm-btn-text">开心收下</text>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
const API_BASE = 'http://localhost:3000/api';

export default {
	data() {
		return {
			activeTab: 'box',
			selectedPrizeIndex: 0,
			remainingStock: 22075,
			showResultModal: false,
			drawnPrizes: [],
			// 严格按照要求的 4 个文件名替换图片路径
			displayPrizeList: [
				{ id: 'iphone', name: 'iPhone手机', fullName: 'iPhone 17 Pro (256GB)', image: '/static/iPhone手机.png' },
				{ id: 'shoes', name: '潮流服饰', fullName: 'Nike Dunk 限定潮鞋/服饰', image: '/static/潮流服饰.png' },
				{ id: 'figures', name: '潮流手办', fullName: '泡泡玛特/盲盒限定手办', image: '/static/潮流手办1.png' },
				{ id: 'skincare', name: '高端护肤', fullName: '海蓝之谜/雅诗兰黛 护肤礼盒', image: '/static/高端护肤.png' }
			],
			tabList: [
				{ id: 'home', name: '首页', icon: '🏠', url: '/pages/index/index' },
				{ id: 'box', name: '盲盒', icon: '🎁', url: '/pages/box/box' },
				{ id: 'shop', name: '商城', icon: '🛍️', url: '/pages/shop/shop' },
				{ id: 'cards', name: '集卡', icon: '🃏', url: '/pages/cards/cards' },
				{ id: 'mine', name: '我的', icon: '👤', url: '/pages/mine/mine' }
			]
		}
	},
	computed: {
		currentSelectedPrize() {
			if (this.displayPrizeList.length > 0 && this.displayPrizeList[this.selectedPrizeIndex]) {
				return this.displayPrizeList[this.selectedPrizeIndex];
			}
			return this.displayPrizeList[0];
		}
	},
	methods: {
		switchTab(tab) {
			this.activeTab = tab.id;
			if (tab.url && tab.id !== 'box') {
				uni.switchTab({
					url: tab.url,
					fail: () => {
						uni.navigateTo({ url: tab.url });
					}
				});
			}
		},
		handleBack() {
			uni.navigateBack({
				fail: () => {
					uni.switchTab({ url: '/pages/index/index' });
				}
			});
		},
		selectPrize(index) {
			this.selectedPrizeIndex = index;
		},
		prevItem() {
			if (this.selectedPrizeIndex > 0) {
				this.selectedPrizeIndex--;
			} else {
				this.selectedPrizeIndex = this.displayPrizeList.length - 1;
			}
		},
		nextItem() {
			if (this.selectedPrizeIndex < this.displayPrizeList.length - 1) {
				this.selectedPrizeIndex++;
			} else {
				this.selectedPrizeIndex = 0;
			}
		},
		startDraw() {
			const targetPrize = this.displayPrizeList[this.selectedPrizeIndex];
			uni.showLoading({ title: '开启盲盒中...' });

			uni.request({
				url: `${API_BASE}/box/draw`,
				method: 'POST',
				header: {
					'Content-Type': 'application/json'
				},
				data: {
					userId: 'U1001',
					targetCategory: targetPrize.name,
					count: 1
				},
				success: (res) => {
					uni.hideLoading();
					if (res.statusCode === 200 && res.data && res.data.code === 200) {
						const drawData = res.data.data || res.data;
						const results = drawData.results || [];

						if (results.length > 0) {
							this.drawnPrizes = results.map(item => ({
								name: item.name,
								rarity: item.rarity || item.type || 'SR'
							}));
						} else {
							this.drawnPrizes = [
								{ name: drawData.name || '精选卡片', rarity: drawData.rarity || 'SR' }
							];
						}

						if (drawData.remainingTotalStock !== undefined) {
							this.remainingStock = drawData.remainingTotalStock;
						} else {
							this.remainingStock = Math.max(0, this.remainingStock - 1);
						}

						this.showResultModal = true;
					} else {
						uni.showToast({
							title: res.data.message || '抽奖失败，请检查后台配置',
							icon: 'none'
						});
					}
				},
				fail: (err) => {
					uni.hideLoading();
					uni.showToast({
						title: '无法连接后端服务，请确认 server.js 已启动',
						icon: 'none'
					});
				}
			});
		},
		closeModal() {
			this.showResultModal = false;
		}
	}
}
</script>

<style>
/* 页面基础容器 */
.page-container {
	width: 100%;
	height: 100vh;
	display: flex;
	flex-direction: column;
	background-color: #030616;
	position: relative;
}

.container {
	flex: 1;
	background-color: #030616;
}

.hero-stage-full {
	width: 100%;
	position: relative;
	align-items: center;
}

.box-bg-full-img {
	width: 100%;
	display: block;
}

.nav-header {
	position: absolute;
	top: 0px;
	left: 0px;
	right: 0px;
	flex-direction: row;
	justify-content: space-between;
	align-items: center;
	padding-top: 12px;
	padding-bottom: 8px;
	padding-left: 12px;
	padding-right: 12px;
	z-index: 20;
}

.back-btn {
	font-size: 24px;
	color: #ffffff;
	font-weight: bold;
}

.placeholder-box {
	width: 24px;
}

.slogan-box {
	position: absolute;
	top: 18px;
	align-self: center;
	flex-direction: column;
	align-items: center;
	z-index: 20;
	padding-top: 8px;
	padding-bottom: 8px;
	padding-left: 16px;
	padding-right: 16px;
	border-radius: 12px;
	background-color: rgba(8, 12, 36, 0.4);
	backdrop-filter: blur(8px);
	border-width: 1px;
	border-style: solid;
	border-color: rgba(168, 85, 247, 0.5);
	box-shadow: 0 0 10px rgba(168, 85, 247, 0.25), inset 0 0 6px rgba(56, 189, 248, 0.1);
}

.slogan-header-title {
	font-size: 15px;
	font-weight: 900;
	color: #ffffff;
	margin-bottom: 4px;
	letter-spacing: 1px;
}

.slogan-main {
	font-size: 13px;
	font-weight: bold;
	color: #ffffff;
}

.highlight-purple {
	color: #e0e7ff;
	background-color: rgba(168, 85, 247, 0.5);
	padding-left: 6px;
	padding-right: 6px;
	padding-top: 1px;
	padding-bottom: 1px;
	border-radius: 4px;
}

.slogan-sub {
	font-size: 9px;
	color: #a5b4fc;
	margin-top: 4px;
}

.arrow-btn {
	position: absolute;
	top: 52%;
	transform: translateY(-50%);
	width: 32px;
	height: 32px;
	border-radius: 16px;
	background-color: rgba(15, 23, 42, 0.65);
	border-width: 1px;
	border-style: solid;
	border-color: rgba(56, 189, 248, 0.6);
	align-items: center;
	justify-content: center;
	z-index: 20;
}

.left-arrow {
	left: 12px;
}

.right-arrow {
	right: 12px;
}

.arrow-icon {
	color: #ffffff;
	font-size: 18px;
	font-weight: bold;
}

.prize-tag-card {
	position: absolute;
	bottom: 12px;
	background-color: rgba(10, 15, 45, 0.85);
	border-width: 1.5px;
	border-style: solid;
	border-color: #a855f7;
	border-radius: 20px;
	padding-top: 6px;
	padding-bottom: 6px;
	padding-left: 20px;
	padding-right: 20px;
	flex-direction: column;
	align-items: center;
	z-index: 20;
}

.prize-tag-title {
	font-size: 14px;
	font-weight: bold;
	color: #ffffff;
}

.hot-badge {
	flex-direction: row;
	align-items: center;
	background-color: #f59e0b;
	border-radius: 10px;
	padding-left: 8px;
	padding-right: 8px;
	padding-top: 1px;
	padding-bottom: 1px;
	margin-top: 3px;
}

.fire-icon {
	font-size: 9px;
	margin-right: 2px;
}

.hot-text {
	font-size: 9px;
	color: #000000;
	font-weight: bold;
}

.content-body {
	padding-left: 10px;
	padding-right: 10px;
}

/* 4格大奖展示区块：优化高宽，确保新图片清晰放大显示 */
.prize-select-section {
	margin-top: 10px;
	background-color: rgba(11, 17, 43, 0.9);
	border-width: 1px;
	border-style: solid;
	border-color: #1e293b;
	border-radius: 14px;
	padding: 10px 8px;
}

.prize-grid-wrapper {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	align-items: center;
	width: 100%;
}

.prize-item-card {
	width: 23%;
	height: 88px;
	border-radius: 10px;
	background-color: #0d1527;
	border-width: 1.5px;
	border-style: solid;
	border-color: #1d283a;
	padding: 8px 4px;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: space-between;
	box-sizing: border-box;
}

.prize-item-active {
	border-color: #ec4899;
	background-color: rgba(236, 72, 153, 0.15);
	box-shadow: 0 0 10px rgba(236, 72, 153, 0.5);
}

.prize-img-box {
	width: 50px;
	height: 50px;
	display: flex;
	align-items: center;
	justify-content: center;
}

.prize-img {
	width: 100%;
	height: 100%;
}

.prize-name {
	font-size: 11px;
	color: #ffffff;
	font-weight: bold;
	text-align: center;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap;
	width: 100%;
}

.draw-action-card {
	margin-top: 10px;
	background-color: rgba(11, 17, 43, 0.95);
	border-width: 1px;
	border-style: solid;
	border-color: #1d2d73;
	border-radius: 14px;
	padding: 12px;
}

.card-top-info {
	flex-direction: row;
	justify-content: space-between;
	align-items: flex-start;
}

.info-left {
	flex-direction: column;
}

.box-title {
	font-size: 14px;
	font-weight: bold;
	color: #ffffff;
}

.info-meta {
	flex-direction: row;
	align-items: center;
	margin-top: 6px;
}

.meta-item {
	flex-direction: row;
	align-items: center;
}

.margin-l {
	margin-left: 12px;
}

.meta-icon {
	font-size: 10px;
	margin-right: 3px;
}

.meta-label {
	font-size: 10px;
	color: #94a3b8;
	margin-right: 3px;
}

.meta-price {
	font-size: 11px;
	font-weight: bold;
	color: #f59e0b;
}

.meta-unit {
	font-size: 9px;
	color: #94a3b8;
}

.meta-guarantee {
	font-size: 11px;
	font-weight: bold;
	color: #f59e0b;
}

.remain-badge {
	background-color: rgba(30, 41, 59, 0.8);
	border-radius: 12px;
	padding-top: 3px;
	padding-bottom: 3px;
	padding-left: 8px;
	padding-right: 8px;
	border-width: 1px;
	border-style: solid;
	border-color: #334155;
}

.remain-text {
	font-size: 9px;
	color: #94a3b8;
}

.remain-num {
	color: #ffffff;
	font-weight: bold;
}

.draw-btn {
	margin-top: 12px;
	background: linear-gradient(90deg, #ec4899 0%, #f43f5e 50%, #f59e0b 100%);
	border-radius: 22px;
	height: 44px;
	align-items: center;
	justify-content: center;
}

.draw-btn-text {
	font-size: 16px;
	font-weight: 900;
	color: #ffffff;
	letter-spacing: 1px;
}

.guarantee-tips {
	font-size: 8px;
	color: #64748b;
	text-align: center;
	margin-top: 8px;
}

.bottom-safe-space {
	height: 70px;
}

.custom-tabbar {
	position: fixed;
	bottom: 0;
	left: 0;
	right: 0;
	height: 56px;
	background-color: #080c1d;
	border-top: 1px solid #1a2238;
	display: flex;
	flex-direction: row;
	justify-content: space-around;
	align-items: center;
	z-index: 100;
	padding-bottom: env(safe-area-inset-bottom);
}

.tabbar-item {
	flex: 1;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	height: 100%;
}

.tabbar-icon {
	font-size: 18px;
	margin-bottom: 2px;
	opacity: 0.6;
}

.tabbar-label {
	font-size: 10px;
	color: #64748b;
}

.tabbar-item-active .tabbar-icon {
	opacity: 1;
}

.tabbar-item-active .tabbar-label {
	color: #a855f7;
	font-weight: bold;
}

.result-modal-mask {
	position: fixed;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
	background-color: rgba(0, 0, 0, 0.75);
	align-items: center;
	justify-content: center;
	z-index: 999;
}

.result-modal-content {
	width: 280px;
	background-color: #0f172a;
	border-width: 1px;
	border-style: solid;
	border-color: #a855f7;
	border-radius: 16px;
	padding: 20px;
	align-items: center;
}

.modal-title {
	font-size: 18px;
	font-weight: bold;
	color: #ffffff;
	margin-bottom: 16px;
}

.prize-display-list {
	width: 100%;
	margin-bottom: 16px;
}

.prize-result-item {
	flex-direction: row;
	align-items: center;
	background-color: rgba(30, 41, 59, 0.8);
	border-radius: 8px;
	padding: 8px 12px;
	margin-bottom: 8px;
}

.prize-type-badge {
	font-size: 10px;
	font-weight: bold;
	color: #ffffff;
	background-color: #ec4899;
	border-radius: 4px;
	padding-left: 6px;
	padding-right: 6px;
	padding-top: 2px;
	padding-bottom: 2px;
	margin-right: 10px;
}

.prize-result-name {
	font-size: 12px;
	color: #ffffff;
	font-weight: bold;
}

.modal-confirm-btn {
	background: linear-gradient(90deg, #ec4899 0%, #f43f5e 100%);
	border-radius: 20px;
	padding-top: 8px;
	padding-bottom: 8px;
	padding-left: 28px;
	padding-right: 28px;
}

.confirm-btn-text {
	font-size: 14px;
	font-weight: bold;
	color: #ffffff;
}
</style>

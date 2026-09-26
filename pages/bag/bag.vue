<template>
	<view class="container">
		<!-- 顶部背包容量概览 -->
		<view class="bag-header-card">
			<view class="header-info">
				<text class="header-title">我的赛博背包</text>
				<text class="capacity-text">容量 8 / 50</text>
			</view>
			<view class="capacity-bar-bg">
				<view class="capacity-bar-fill" style="width: 16%;"></view>
			</view>
		</view>

		<!-- 分类切换 Tab -->
		<view class="filter-tabs">
			<view
				class="tab-btn"
				v-for="(tab, index) in tabs"
				:key="index"
				:class="{ 'active': activeTab === index }"
				@click="activeTab = index"
			>
				<text class="tab-label">{{ tab }}</text>
			</view>
		</view>

		<!-- 物品网格列表 -->
		<view class="goods-grid">
			<view
				class="goods-item"
				v-for="(item, index) in filteredList"
				:key="index"
			>
				<!-- 数量角标 -->
				<view class="count-badge">
					<text class="badge-text">x{{ item.count }}</text>
				</view>

				<!-- 物品图标 -->
				<view class="goods-icon-wrapper">
					<text class="goods-emoji">{{ item.icon }}</text>
				</view>

				<!-- 名称与描述 -->
				<text class="goods-title">{{ item.name }}</text>
				<text class="goods-desc">{{ item.desc }}</text>

				<!-- 操作按钮区 -->
				<view class="action-btns">
					<button class="btn-action btn-decompose" @click="decompose(item)">
						<text class="btn-text">分解</text>
					</button>
					<button class="btn-action btn-use" @click="useItem(item)">
						<text class="btn-text">使用</text>
					</button>
				</view>
			</view>
		</view>

		<!-- 底部霓虹 TabBar（背包 current 为 3） -->
		<NeonTabBar :current="3" />
	</view>
</template>

<script>
import NeonTabBar from '@/components/NeonTabBar.uvue';

export default {
	components: {
		NeonTabBar
	},
	data() {
		return {
			activeTab: 0,
			tabs: ['全部', '盲盒', '卡牌', '道具'],
			itemList: [
				{ id: 1, name: '赛博姬限定手办', type: '盲盒', count: 1, icon: '🤖', desc: '未拆封·可兑换实物' },
				{ id: 2, name: 'iPhone 17 兑换券', type: '道具', count: 1, icon: '📱', desc: '提货后顺丰包邮' },
				{ id: 3, name: '赛博霓虹姬 [SSR]', type: '卡牌', count: 1, icon: '🎴', desc: '可用于套卡合成' },
				{ id: 4, name: 'SSR 必中合成卡', type: '道具', count: 2, icon: '🃏', desc: '合成时概率100%' },
				{ id: 5, name: '50元透支抵扣券', type: '道具', count: 3, icon: '🎟️', desc: '开盒时自动抵扣' }
			]
		}
	},
	computed: {
		filteredList() {
			if (this.activeTab === 0) return this.itemList;
			const targetType = this.tabs[this.activeTab];
			return this.itemList.filter(item => item.type === targetType);
		}
	},
	methods: {
		useItem(item) {
			uni.showToast({
				title: '已使用 ' + item.name,
				icon: 'none'
			});
		},
		decompose(item) {
			uni.showModal({
				title: '分解提示',
				content: '确认将 ' + item.name + ' 分解为积分吗？',
				success: (res) => {
					if (res.confirm) {
						uni.showToast({
							title: '获得 +500 积分',
							icon: 'success'
						});
					}
				}
			});
		}
	}
}
</script>

<style>
.container {
	min-height: 100vh;
	background-color: #07091e;
	padding: 16px;
	padding-bottom: 80px; /* 留出底部导航空间 */
	box-sizing: border-box;
}

/* 顶部容量卡片 */
.bag-header-card {
	background: linear-gradient(135deg, #181c4a 0%, #2a1b4e 100%);
	border: 1px solid #3c438c;
	border-radius: 16px;
	padding: 16px;
	margin-bottom: 16px;
}

.header-info {
	display: flex;
	flex-direction: row;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 10px;
}

.header-title {
	font-size: 18px;
	font-weight: bold;
	color: #ffffff;
}

.capacity-text {
	font-size: 12px;
	color: #e072ff;
	font-weight: bold;
}

.capacity-bar-bg {
	height: 6px;
	background-color: #0f1338;
	border-radius: 3px;
	overflow: hidden;
}

.capacity-bar-fill {
	height: 100%;
	background: linear-gradient(90deg, #8b2bf5 0%, #e072ff 100%);
}

/* 分类切换 Tab */
.filter-tabs {
	display: flex;
	flex-direction: row;
	gap: 10px;
	margin-bottom: 16px;
}

.tab-btn {
	padding: 6px 16px;
	border-radius: 20px;
	background-color: #0f1338;
	border: 1px solid #1c2252;
}

.tab-btn.active {
	background: linear-gradient(90deg, #8b2bf5, #e072ff);
	border-color: transparent;
}

.tab-label {
	font-size: 12px;
	color: #8c93bd;
}

.tab-btn.active .tab-label {
	color: #ffffff;
	font-weight: bold;
}

/* 物品网格 */
.goods-grid {
	display: flex;
	flex-direction: row;
	flex-wrap: wrap;
	justify-content: space-between;
	gap: 12px;
}

.goods-item {
	width: 48%;
	background-color: #0f1338;
	border: 1px solid #1c2252;
	border-radius: 14px;
	padding: 12px;
	box-sizing: border-box;
	display: flex;
	flex-direction: column;
	position: relative;
}

.count-badge {
	position: absolute;
	top: 8px;
	right: 8px;
	background-color: #171b4a;
	border: 1px solid #3c438c;
	padding: 2px 6px;
	border-radius: 8px;
}

.badge-text {
	font-size: 10px;
	color: #ffd700;
	font-weight: bold;
}

.goods-icon-wrapper {
	width: 100%;
	height: 70px;
	display: flex;
	align-items: center;
	justify-content: center;
	background-color: #171b4a;
	border-radius: 10px;
	margin-top: 6px;
	margin-bottom: 8px;
}

.goods-emoji {
	font-size: 36px;
}

.goods-title {
	font-size: 14px;
	font-weight: bold;
	color: #ffffff;
	lines: 1;
	text-overflow: ellipsis;
}

.goods-desc {
	font-size: 11px;
	color: #6c7293;
	margin-top: 2px;
	margin-bottom: 10px;
	lines: 1;
	text-overflow: ellipsis;
}

.action-btns {
	display: flex;
	flex-direction: row;
	gap: 6px;
}

.btn-action {
	flex: 1;
	padding: 4px 0;
	border-radius: 10px;
	border: none;
	display: flex;
	justify-content: center;
	align-items: center;
}

.btn-decompose {
	background-color: #1a1e4a;
	border: 1px solid #2e357b;
}

.btn-use {
	background: linear-gradient(90deg, #ff2a8d 0%, #ff5252 100%);
}

.btn-text {
	color: #ffffff;
	font-size: 11px;
	font-weight: bold;
}
</style>

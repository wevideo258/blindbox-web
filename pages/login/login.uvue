<template>
	<view class="login-container">
		<!-- 顶部背景图 -->
		<image class="top-bg-img" src="/static/user背景.png" mode="widthFix"></image>

		<!-- 头部 Logo 与标语 -->
		<view class="header-section">
			<!-- 缩小后的 Logo 展示 -->
			<view class="logo-box">
				<image class="logo-img" src="/static/logo1.png" mode="widthFix"></image>
			</view>
			<text class="main-title">欢迎来到拾界</text>
			<text class="sub-title">开启你的专属收藏之旅</text>
		</view>

		<!-- 表单区域 -->
		<view class="form-section">
			<!-- 手机号输入框 -->
			<view class="input-item">
				<text class="input-icon">📱</text>
				<input class="input-field" type="number" maxlength="11" v-model="mobile" placeholder="请输入手机号" placeholder-class="ph-style" />
			</view>

			<!-- 验证码输入框 -->
			<view class="input-item">
				<text class="input-icon">🛡️</text>
				<input class="input-field" type="number" maxlength="6" v-model="code" placeholder="请输入验证码" placeholder-class="ph-style" />
				<view class="code-btn" @click="getVerifyCode">
					<text class="code-text">{{ countdown > 0 ? countdown + 's' : '获取验证码' }}</text>
				</view>
			</view>

			<!-- 登录/注册按钮 -->
			<view class="submit-btn" @click="handleLogin">
				<text class="submit-btn-text">登录 / 注册 ›</text>
			</view>
		</view>

		<!-- 第三方登录区域 -->
		<view class="third-party-section">
			<view class="divider-box">
				<view class="divider-line"></view>
				<text class="divider-text">其他登录方式</text>
				<view class="divider-line"></view>
			</view>

			<view class="third-icons">
				<view class="third-btn" @click="thirdLogin('微信')">
					<view class="icon-circle"><text class="third-icon">💬</text></view>
					<text class="third-label">微信</text>
				</view>
				<view class="third-btn" @click="thirdLogin('Apple')">
					<view class="icon-circle"><text class="third-icon">🍎</text></view>
					<text class="third-label">Apple</text>
				</view>
				<view class="third-btn" @click="thirdLogin('账号')">
					<view class="icon-circle"><text class="third-icon">👤</text></view>
					<text class="third-label">账号登录</text>
				</view>
			</view>
		</view>

		<!-- 底部协议 -->
		<view class="protocol-section" @click="agreed = !agreed">
			<text class="checkbox-icon">{{ agreed ? '☑' : '☐' }}</text>
			<text class="protocol-text">我已阅读并同意</text>
			<text class="protocol-link">《用户协议》</text>
			<text class="protocol-text">和</text>
			<text class="protocol-link">《隐私政策》</text>
		</view>
	</view>
</template>

<script setup lang="uts">
import { ref } from 'vue';

const mobile = ref('');
const code = ref('');
const agreed = ref(true); // 默认选中协议，方便体验
const countdown = ref(0);

// 获取验证码
const getVerifyCode = () => {
	if (countdown.value > 0) return;
	countdown.value = 60;
	const timer = setInterval(() => {
		countdown.value--;
		if (countdown.value <= 0) {
			clearInterval(timer);
		}
	}, 1000);
	uni.showToast({ title: '验证码已发送', icon: 'success' });
};

// 点击登录：直接提示成功并跳转至首页
const handleLogin = () => {
	uni.showToast({ title: '登录成功', icon: 'success' });

	setTimeout(() => {
		// 清空当前页面栈并跳转到首页
		uni.reLaunch({
			url: '/pages/index/index'
		});
	}, 500);
};

// 点击第三方登录：同样直接跳转至首页
const thirdLogin = (type: string) => {
	uni.showToast({ title: `${type}登录成功`, icon: 'success' });
	setTimeout(() => {
		uni.reLaunch({
			url: '/pages/index/index'
		});
	}, 500);
};
</script>

<style>
.login-container {
	flex: 1;
	position: relative;
	/* 渐变霓虹深暗背景 */
	background-image: linear-gradient(160deg, #180928 0%, #030616 50%, #081c2f 100%);
	padding: 40px 24px 20px 24px;
	flex-direction: column;
	justify-content: space-between;
	align-items: center;
}

/* 顶部 user背景 图样式 */
.top-bg-img {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	opacity: 0.65;
	z-index: 0;
}

/* 头部样式 */
.header-section {
	align-items: center;
	margin-top: 20px;
	z-index: 1;
}

/* 缩小后的 Logo 尺寸设置 */
.logo-box {
	width: 160px;
	margin-bottom: 12px;
	align-items: center;
	justify-content: center;
}

.logo-img {
	width: 100%;
}

.main-title {
	color: #ffffff;
	font-size: 26px;
	font-weight: bold;
	margin-bottom: 8px;
}

.sub-title {
	color: #94a3b8;
	font-size: 14px;
}

/* 表单样式 */
.form-section {
	width: 100%;
	z-index: 1;
}

.input-item {
	height: 50px;
	background-color: rgba(15, 23, 42, 0.65);
	border-width: 1px;
	border-style: solid;
	border-color: rgba(99, 102, 241, 0.25);
	border-radius: 25px;
	flex-direction: row;
	align-items: center;
	padding: 0 16px;
	margin-bottom: 16px;
}

.input-icon {
	font-size: 18px;
	margin-right: 10px;
}

.input-field {
	flex: 1;
	color: #ffffff;
	font-size: 14px;
}

.ph-style {
	color: #475569;
}

.code-btn {
	border-left-width: 1px;
	border-left-style: solid;
	border-left-color: rgba(51, 65, 85, 0.8);
	padding-left: 12px;
}

.code-text {
	color: #818cf8;
	font-size: 13px;
}

.submit-btn {
	height: 50px;
	background-image: linear-gradient(to right, #a855f7, #3b82f6);
	border-radius: 25px;
	justify-content: center;
	align-items: center;
	margin-top: 10px;
	box-shadow: 0 4px 15px rgba(168, 85, 247, 0.35);
}

.submit-btn-text {
	color: #ffffff;
	font-size: 16px;
	font-weight: bold;
}

/* 第三方登录 */
.third-party-section {
	width: 100%;
	align-items: center;
	z-index: 1;
}

.divider-box {
	flex-direction: row;
	align-items: center;
	margin-bottom: 20px;
}

.divider-line {
	flex: 1;
	height: 1px;
	background-color: rgba(30, 41, 59, 0.8);
}

.divider-text {
	color: #64748b;
	font-size: 12px;
	margin: 0 12px;
}

.third-icons {
	flex-direction: row;
	justify-content: space-around;
	width: 80%;
}

.third-btn {
	align-items: center;
}

.icon-circle {
	width: 48px;
	height: 48px;
	border-radius: 24px;
	border-width: 1px;
	border-style: solid;
	border-color: rgba(56, 189, 248, 0.5);
	justify-content: center;
	align-items: center;
	background-color: rgba(11, 17, 43, 0.8);
	margin-bottom: 6px;
}

.third-icon {
	font-size: 20px;
}

.third-label {
	color: #94a3b8;
	font-size: 12px;
}

/* 底部协议 */
.protocol-section {
	flex-direction: row;
	align-items: center;
	margin-bottom: 10px;
	z-index: 1;
}

.checkbox-icon {
	color: #38bdf8;
	font-size: 16px;
	margin-right: 6px;
}

.protocol-text {
	color: #64748b;
	font-size: 12px;
}

.protocol-link {
	color: #38bdf8;
	font-size: 12px;
}
</style>

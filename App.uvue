<script setup lang="uts">
	// #ifdef APP-ANDROID || APP-HARMONY
	let firstBackTime = 0
	// #endif

	onLaunch(() => {
		console.log('App Launch')
	})

	onShow(() => {
		console.log('App Show')
	})

	onHide(() => {
		console.log('App Hide')
	})
</script>

<style>
	/* 每个页面公共 CSS */
	.uni-row {
		flex-direction: row;
	}

	.uni-column {
		flex-direction: column;
	}

	/* 隐藏 Web 端原生顶部导航栏 */
	uni-page-head,
	.uni-page-head,
	.uni-page-head-placeholder {
		display: none !important;
		height: 0 !important;
	}

	/* 消除页面包裹层偏移 */
	.uni-page-wrapper,
	uni-page-body {
		height: 100% !important;
		min-height: 100vh !important;
		padding-top: 0 !important;
		margin-top: 0 !important;
	}
</style>

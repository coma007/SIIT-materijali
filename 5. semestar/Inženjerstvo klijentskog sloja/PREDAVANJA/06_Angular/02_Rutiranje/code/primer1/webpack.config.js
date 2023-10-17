const fs = require('fs');
const path = require('path');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const ProgressPlugin = require('webpack/lib/ProgressPlugin');
const CircularDependencyPlugin = require('circular-dependency-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const autoprefixer = require('autoprefixer');
const postcssUrl = require('postcss-url');
const cssnano = require('cssnano');
const customProperties = require('postcss-custom-properties');

const { NoEmitOnErrorsPlugin, SourceMapDevToolPlugin, NamedModulesPlugin } = require('webpack');
const { NamedLazyChunksWebpackPlugin, BaseHrefWebpackPlugin } = require('@angular/cli/plugins/webpack');
const { CommonsChunkPlugin } = require('webpack').optimize;
const { AngularCompilerPlugin } = require('@ngtools/webpack');

const nodeModules = path.join(process.cwd(), 'node_modules');
const realNodeModules = fs.realpathSync(nodeModules);
const genDirNodeModules = path.join(process.cwd(), 'src', '$$_gendir', 'node_modules');
const entryPoints = ["inline","polyfills","sw-register","styles","vendor","main"];
const minimizeCss = false;
const baseHref = "";
const deployUrl = "";
const postcssPlugins = function () {
        // safe settings based on: https://github.com/ben-eb/cssnano/issues/358#issuecomment-283696193
        const importantCommentRe = /@preserve|@license|[@#]\s*source(?:Mapping)?URL|^!/i;
        const minimizeOptions = {
            autoprefixer: false,
            safe: true,
            mergeLonghand: false,
            discardComments: { remove: (comment) => !importantCommentRe.test(comment) }
        };
        return [
            postcssUrl({
                url: (URL) => {
                    // Only convert root relative URLs, which CSS-Loader won't process into require().
                    if (!URL.startsWith('/') || URL.startsWith('//')) {
                        return URL;
                    }
                    if (deployUrl.match(/:\/\//)) {
                        // If deployUrl contains a scheme, ignore baseHref use deployUrl as is.
                        return `${deployUrl.replace(/\/$/, '')}${URL}`;
                    }
                    else if (baseHref.match(/:\/\//)) {
                        // If baseHref contains a scheme, include it as is.
                        return baseHref.replace(/\/$/, '') +
                            `/${deployUrl}/${URL}`.replace(/\/\/+/g, '/');
                    }
                    else {
                        // Join together base-href, deploy-url and the original URL.
                        // Also dedupe multiple slashes into single ones.
                        return `/${baseHref}/${deployUrl}/${URL}`.replace(/\/\/+/g, '/');
                    }
                }
            }),
            autoprefixer(),
            customProperties({ preserve: true })
        ].concat(minimizeCss ? [cssnano(minimizeOptions)] : []);
    };




module.exports = {
  "resolve": {
    "extensions": [
      ".ts",
      ".js"
    ],
    "modules": [
      "./node_modules",
      "./node_modules"
    ],
    "symlinks": true,
    "alias": {
      "rxjs/util/tryCatch": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\tryCatch.js",
      "rxjs/util/toSubscriber": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\toSubscriber.js",
      "rxjs/util/subscribeToResult": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\subscribeToResult.js",
      "rxjs/util/root": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\root.js",
      "rxjs/util/pipe": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\pipe.js",
      "rxjs/util/not": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\not.js",
      "rxjs/util/noop": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\noop.js",
      "rxjs/util/isScheduler": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\isScheduler.js",
      "rxjs/util/isPromise": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\isPromise.js",
      "rxjs/util/isObject": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\isObject.js",
      "rxjs/util/isNumeric": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\isNumeric.js",
      "rxjs/util/isFunction": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\isFunction.js",
      "rxjs/util/isDate": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\isDate.js",
      "rxjs/util/isArrayLike": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\isArrayLike.js",
      "rxjs/util/isArray": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\isArray.js",
      "rxjs/util/identity": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\identity.js",
      "rxjs/util/errorObject": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\errorObject.js",
      "rxjs/util/assign": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\assign.js",
      "rxjs/util/applyMixins": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\applyMixins.js",
      "rxjs/util/UnsubscriptionError": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\UnsubscriptionError.js",
      "rxjs/util/TimeoutError": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\TimeoutError.js",
      "rxjs/util/Set": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\Set.js",
      "rxjs/util/ObjectUnsubscribedError": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\ObjectUnsubscribedError.js",
      "rxjs/util/MapPolyfill": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\MapPolyfill.js",
      "rxjs/util/Map": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\Map.js",
      "rxjs/util/Immediate": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\Immediate.js",
      "rxjs/util/FastMap": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\FastMap.js",
      "rxjs/util/EmptyError": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\EmptyError.js",
      "rxjs/util/ArgumentOutOfRangeError": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\ArgumentOutOfRangeError.js",
      "rxjs/util/AnimationFrame": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\util\\AnimationFrame.js",
      "rxjs/testing/TestScheduler": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\testing\\TestScheduler.js",
      "rxjs/testing/TestMessage": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\testing\\TestMessage.js",
      "rxjs/testing/SubscriptionLoggable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\testing\\SubscriptionLoggable.js",
      "rxjs/testing/SubscriptionLog": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\testing\\SubscriptionLog.js",
      "rxjs/testing/HotObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\testing\\HotObservable.js",
      "rxjs/testing/ColdObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\testing\\ColdObservable.js",
      "rxjs/symbol/rxSubscriber": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\symbol\\rxSubscriber.js",
      "rxjs/symbol/observable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\symbol\\observable.js",
      "rxjs/symbol/iterator": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\symbol\\iterator.js",
      "rxjs/scheduler/queue": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\scheduler\\queue.js",
      "rxjs/scheduler/async": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\scheduler\\async.js",
      "rxjs/scheduler/asap": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\scheduler\\asap.js",
      "rxjs/scheduler/animationFrame": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\scheduler\\animationFrame.js",
      "rxjs/scheduler/VirtualTimeScheduler": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\scheduler\\VirtualTimeScheduler.js",
      "rxjs/scheduler/QueueScheduler": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\scheduler\\QueueScheduler.js",
      "rxjs/scheduler/QueueAction": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\scheduler\\QueueAction.js",
      "rxjs/scheduler/AsyncScheduler": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\scheduler\\AsyncScheduler.js",
      "rxjs/scheduler/AsyncAction": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\scheduler\\AsyncAction.js",
      "rxjs/scheduler/AsapScheduler": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\scheduler\\AsapScheduler.js",
      "rxjs/scheduler/AsapAction": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\scheduler\\AsapAction.js",
      "rxjs/scheduler/AnimationFrameScheduler": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\scheduler\\AnimationFrameScheduler.js",
      "rxjs/scheduler/AnimationFrameAction": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\scheduler\\AnimationFrameAction.js",
      "rxjs/scheduler/Action": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\scheduler\\Action.js",
      "rxjs/operators/zipAll": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\zipAll.js",
      "rxjs/operators/zip": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\zip.js",
      "rxjs/operators/withLatestFrom": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\withLatestFrom.js",
      "rxjs/operators/windowWhen": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\windowWhen.js",
      "rxjs/operators/windowToggle": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\windowToggle.js",
      "rxjs/operators/windowTime": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\windowTime.js",
      "rxjs/operators/windowCount": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\windowCount.js",
      "rxjs/operators/window": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\window.js",
      "rxjs/operators/toArray": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\toArray.js",
      "rxjs/operators/timestamp": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\timestamp.js",
      "rxjs/operators/timeoutWith": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\timeoutWith.js",
      "rxjs/operators/timeout": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\timeout.js",
      "rxjs/operators/timeInterval": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\timeInterval.js",
      "rxjs/operators/throttleTime": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\throttleTime.js",
      "rxjs/operators/throttle": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\throttle.js",
      "rxjs/operators/tap": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\tap.js",
      "rxjs/operators/takeWhile": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\takeWhile.js",
      "rxjs/operators/takeUntil": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\takeUntil.js",
      "rxjs/operators/takeLast": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\takeLast.js",
      "rxjs/operators/take": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\take.js",
      "rxjs/operators/switchMapTo": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\switchMapTo.js",
      "rxjs/operators/switchMap": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\switchMap.js",
      "rxjs/operators/switchAll": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\switchAll.js",
      "rxjs/operators/subscribeOn": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\subscribeOn.js",
      "rxjs/operators/startWith": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\startWith.js",
      "rxjs/operators/skipWhile": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\skipWhile.js",
      "rxjs/operators/skipUntil": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\skipUntil.js",
      "rxjs/operators/skipLast": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\skipLast.js",
      "rxjs/operators/skip": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\skip.js",
      "rxjs/operators/single": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\single.js",
      "rxjs/operators/shareReplay": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\shareReplay.js",
      "rxjs/operators/share": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\share.js",
      "rxjs/operators/sequenceEqual": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\sequenceEqual.js",
      "rxjs/operators/scan": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\scan.js",
      "rxjs/operators/sampleTime": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\sampleTime.js",
      "rxjs/operators/sample": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\sample.js",
      "rxjs/operators/retryWhen": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\retryWhen.js",
      "rxjs/operators/retry": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\retry.js",
      "rxjs/operators/repeatWhen": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\repeatWhen.js",
      "rxjs/operators/repeat": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\repeat.js",
      "rxjs/operators/refCount": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\refCount.js",
      "rxjs/operators/reduce": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\reduce.js",
      "rxjs/operators/race": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\race.js",
      "rxjs/operators/publishReplay": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\publishReplay.js",
      "rxjs/operators/publishLast": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\publishLast.js",
      "rxjs/operators/publishBehavior": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\publishBehavior.js",
      "rxjs/operators/publish": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\publish.js",
      "rxjs/operators/pluck": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\pluck.js",
      "rxjs/operators/partition": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\partition.js",
      "rxjs/operators/pairwise": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\pairwise.js",
      "rxjs/operators/onErrorResumeNext": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\onErrorResumeNext.js",
      "rxjs/operators/observeOn": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\observeOn.js",
      "rxjs/operators/multicast": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\multicast.js",
      "rxjs/operators/min": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\min.js",
      "rxjs/operators/mergeScan": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\mergeScan.js",
      "rxjs/operators/mergeMapTo": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\mergeMapTo.js",
      "rxjs/operators/mergeMap": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\mergeMap.js",
      "rxjs/operators/mergeAll": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\mergeAll.js",
      "rxjs/operators/merge": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\merge.js",
      "rxjs/operators/max": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\max.js",
      "rxjs/operators/materialize": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\materialize.js",
      "rxjs/operators/mapTo": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\mapTo.js",
      "rxjs/operators/map": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\map.js",
      "rxjs/operators/last": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\last.js",
      "rxjs/operators/isEmpty": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\isEmpty.js",
      "rxjs/operators/ignoreElements": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\ignoreElements.js",
      "rxjs/operators/groupBy": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\groupBy.js",
      "rxjs/operators/first": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\first.js",
      "rxjs/operators/findIndex": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\findIndex.js",
      "rxjs/operators/find": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\find.js",
      "rxjs/operators/finalize": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\finalize.js",
      "rxjs/operators/filter": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\filter.js",
      "rxjs/operators/expand": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\expand.js",
      "rxjs/operators/exhaustMap": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\exhaustMap.js",
      "rxjs/operators/exhaust": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\exhaust.js",
      "rxjs/operators/every": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\every.js",
      "rxjs/operators/elementAt": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\elementAt.js",
      "rxjs/operators/distinctUntilKeyChanged": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\distinctUntilKeyChanged.js",
      "rxjs/operators/distinctUntilChanged": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\distinctUntilChanged.js",
      "rxjs/operators/distinct": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\distinct.js",
      "rxjs/operators/dematerialize": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\dematerialize.js",
      "rxjs/operators/delayWhen": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\delayWhen.js",
      "rxjs/operators/delay": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\delay.js",
      "rxjs/operators/defaultIfEmpty": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\defaultIfEmpty.js",
      "rxjs/operators/debounceTime": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\debounceTime.js",
      "rxjs/operators/debounce": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\debounce.js",
      "rxjs/operators/count": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\count.js",
      "rxjs/operators/concatMapTo": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\concatMapTo.js",
      "rxjs/operators/concatMap": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\concatMap.js",
      "rxjs/operators/concatAll": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\concatAll.js",
      "rxjs/operators/concat": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\concat.js",
      "rxjs/operators/combineLatest": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\combineLatest.js",
      "rxjs/operators/combineAll": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\combineAll.js",
      "rxjs/operators/catchError": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\catchError.js",
      "rxjs/operators/bufferWhen": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\bufferWhen.js",
      "rxjs/operators/bufferToggle": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\bufferToggle.js",
      "rxjs/operators/bufferTime": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\bufferTime.js",
      "rxjs/operators/bufferCount": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\bufferCount.js",
      "rxjs/operators/buffer": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\buffer.js",
      "rxjs/operators/auditTime": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\auditTime.js",
      "rxjs/operators/audit": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators\\audit.js",
      "rxjs/operators": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operators.js",
      "rxjs/operator/zipAll": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\zipAll.js",
      "rxjs/operator/zip": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\zip.js",
      "rxjs/operator/withLatestFrom": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\withLatestFrom.js",
      "rxjs/operator/windowWhen": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\windowWhen.js",
      "rxjs/operator/windowToggle": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\windowToggle.js",
      "rxjs/operator/windowTime": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\windowTime.js",
      "rxjs/operator/windowCount": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\windowCount.js",
      "rxjs/operator/window": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\window.js",
      "rxjs/operator/toPromise": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\toPromise.js",
      "rxjs/operator/toArray": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\toArray.js",
      "rxjs/operator/timestamp": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\timestamp.js",
      "rxjs/operator/timeoutWith": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\timeoutWith.js",
      "rxjs/operator/timeout": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\timeout.js",
      "rxjs/operator/timeInterval": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\timeInterval.js",
      "rxjs/operator/throttleTime": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\throttleTime.js",
      "rxjs/operator/throttle": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\throttle.js",
      "rxjs/operator/takeWhile": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\takeWhile.js",
      "rxjs/operator/takeUntil": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\takeUntil.js",
      "rxjs/operator/takeLast": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\takeLast.js",
      "rxjs/operator/take": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\take.js",
      "rxjs/operator/switchMapTo": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\switchMapTo.js",
      "rxjs/operator/switchMap": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\switchMap.js",
      "rxjs/operator/switch": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\switch.js",
      "rxjs/operator/subscribeOn": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\subscribeOn.js",
      "rxjs/operator/startWith": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\startWith.js",
      "rxjs/operator/skipWhile": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\skipWhile.js",
      "rxjs/operator/skipUntil": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\skipUntil.js",
      "rxjs/operator/skipLast": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\skipLast.js",
      "rxjs/operator/skip": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\skip.js",
      "rxjs/operator/single": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\single.js",
      "rxjs/operator/shareReplay": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\shareReplay.js",
      "rxjs/operator/share": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\share.js",
      "rxjs/operator/sequenceEqual": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\sequenceEqual.js",
      "rxjs/operator/scan": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\scan.js",
      "rxjs/operator/sampleTime": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\sampleTime.js",
      "rxjs/operator/sample": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\sample.js",
      "rxjs/operator/retryWhen": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\retryWhen.js",
      "rxjs/operator/retry": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\retry.js",
      "rxjs/operator/repeatWhen": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\repeatWhen.js",
      "rxjs/operator/repeat": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\repeat.js",
      "rxjs/operator/reduce": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\reduce.js",
      "rxjs/operator/race": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\race.js",
      "rxjs/operator/publishReplay": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\publishReplay.js",
      "rxjs/operator/publishLast": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\publishLast.js",
      "rxjs/operator/publishBehavior": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\publishBehavior.js",
      "rxjs/operator/publish": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\publish.js",
      "rxjs/operator/pluck": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\pluck.js",
      "rxjs/operator/partition": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\partition.js",
      "rxjs/operator/pairwise": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\pairwise.js",
      "rxjs/operator/onErrorResumeNext": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\onErrorResumeNext.js",
      "rxjs/operator/observeOn": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\observeOn.js",
      "rxjs/operator/multicast": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\multicast.js",
      "rxjs/operator/min": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\min.js",
      "rxjs/operator/mergeScan": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\mergeScan.js",
      "rxjs/operator/mergeMapTo": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\mergeMapTo.js",
      "rxjs/operator/mergeMap": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\mergeMap.js",
      "rxjs/operator/mergeAll": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\mergeAll.js",
      "rxjs/operator/merge": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\merge.js",
      "rxjs/operator/max": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\max.js",
      "rxjs/operator/materialize": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\materialize.js",
      "rxjs/operator/mapTo": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\mapTo.js",
      "rxjs/operator/map": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\map.js",
      "rxjs/operator/let": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\let.js",
      "rxjs/operator/last": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\last.js",
      "rxjs/operator/isEmpty": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\isEmpty.js",
      "rxjs/operator/ignoreElements": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\ignoreElements.js",
      "rxjs/operator/groupBy": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\groupBy.js",
      "rxjs/operator/first": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\first.js",
      "rxjs/operator/findIndex": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\findIndex.js",
      "rxjs/operator/find": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\find.js",
      "rxjs/operator/finally": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\finally.js",
      "rxjs/operator/filter": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\filter.js",
      "rxjs/operator/expand": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\expand.js",
      "rxjs/operator/exhaustMap": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\exhaustMap.js",
      "rxjs/operator/exhaust": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\exhaust.js",
      "rxjs/operator/every": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\every.js",
      "rxjs/operator/elementAt": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\elementAt.js",
      "rxjs/operator/do": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\do.js",
      "rxjs/operator/distinctUntilKeyChanged": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\distinctUntilKeyChanged.js",
      "rxjs/operator/distinctUntilChanged": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\distinctUntilChanged.js",
      "rxjs/operator/distinct": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\distinct.js",
      "rxjs/operator/dematerialize": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\dematerialize.js",
      "rxjs/operator/delayWhen": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\delayWhen.js",
      "rxjs/operator/delay": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\delay.js",
      "rxjs/operator/defaultIfEmpty": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\defaultIfEmpty.js",
      "rxjs/operator/debounceTime": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\debounceTime.js",
      "rxjs/operator/debounce": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\debounce.js",
      "rxjs/operator/count": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\count.js",
      "rxjs/operator/concatMapTo": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\concatMapTo.js",
      "rxjs/operator/concatMap": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\concatMap.js",
      "rxjs/operator/concatAll": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\concatAll.js",
      "rxjs/operator/concat": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\concat.js",
      "rxjs/operator/combineLatest": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\combineLatest.js",
      "rxjs/operator/combineAll": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\combineAll.js",
      "rxjs/operator/catch": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\catch.js",
      "rxjs/operator/bufferWhen": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\bufferWhen.js",
      "rxjs/operator/bufferToggle": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\bufferToggle.js",
      "rxjs/operator/bufferTime": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\bufferTime.js",
      "rxjs/operator/bufferCount": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\bufferCount.js",
      "rxjs/operator/buffer": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\buffer.js",
      "rxjs/operator/auditTime": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\auditTime.js",
      "rxjs/operator/audit": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\operator\\audit.js",
      "rxjs/observable/zip": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\zip.js",
      "rxjs/observable/using": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\using.js",
      "rxjs/observable/timer": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\timer.js",
      "rxjs/observable/throw": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\throw.js",
      "rxjs/observable/range": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\range.js",
      "rxjs/observable/race": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\race.js",
      "rxjs/observable/pairs": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\pairs.js",
      "rxjs/observable/onErrorResumeNext": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\onErrorResumeNext.js",
      "rxjs/observable/of": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\of.js",
      "rxjs/observable/never": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\never.js",
      "rxjs/observable/merge": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\merge.js",
      "rxjs/observable/interval": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\interval.js",
      "rxjs/observable/if": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\if.js",
      "rxjs/observable/generate": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\generate.js",
      "rxjs/observable/fromPromise": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\fromPromise.js",
      "rxjs/observable/fromEventPattern": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\fromEventPattern.js",
      "rxjs/observable/fromEvent": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\fromEvent.js",
      "rxjs/observable/from": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\from.js",
      "rxjs/observable/forkJoin": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\forkJoin.js",
      "rxjs/observable/empty": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\empty.js",
      "rxjs/observable/dom/webSocket": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\dom\\webSocket.js",
      "rxjs/observable/dom/ajax": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\dom\\ajax.js",
      "rxjs/observable/dom/WebSocketSubject": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\dom\\WebSocketSubject.js",
      "rxjs/observable/dom/AjaxObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\dom\\AjaxObservable.js",
      "rxjs/observable/defer": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\defer.js",
      "rxjs/observable/concat": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\concat.js",
      "rxjs/observable/combineLatest": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\combineLatest.js",
      "rxjs/observable/bindNodeCallback": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\bindNodeCallback.js",
      "rxjs/observable/bindCallback": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\bindCallback.js",
      "rxjs/observable/UsingObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\UsingObservable.js",
      "rxjs/observable/TimerObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\TimerObservable.js",
      "rxjs/observable/SubscribeOnObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\SubscribeOnObservable.js",
      "rxjs/observable/ScalarObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\ScalarObservable.js",
      "rxjs/observable/RangeObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\RangeObservable.js",
      "rxjs/observable/PromiseObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\PromiseObservable.js",
      "rxjs/observable/PairsObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\PairsObservable.js",
      "rxjs/observable/NeverObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\NeverObservable.js",
      "rxjs/observable/IteratorObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\IteratorObservable.js",
      "rxjs/observable/IntervalObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\IntervalObservable.js",
      "rxjs/observable/IfObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\IfObservable.js",
      "rxjs/observable/GenerateObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\GenerateObservable.js",
      "rxjs/observable/FromObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\FromObservable.js",
      "rxjs/observable/FromEventPatternObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\FromEventPatternObservable.js",
      "rxjs/observable/FromEventObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\FromEventObservable.js",
      "rxjs/observable/ForkJoinObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\ForkJoinObservable.js",
      "rxjs/observable/ErrorObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\ErrorObservable.js",
      "rxjs/observable/EmptyObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\EmptyObservable.js",
      "rxjs/observable/DeferObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\DeferObservable.js",
      "rxjs/observable/ConnectableObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\ConnectableObservable.js",
      "rxjs/observable/BoundNodeCallbackObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\BoundNodeCallbackObservable.js",
      "rxjs/observable/BoundCallbackObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\BoundCallbackObservable.js",
      "rxjs/observable/ArrayObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\ArrayObservable.js",
      "rxjs/observable/ArrayLikeObservable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\observable\\ArrayLikeObservable.js",
      "rxjs/interfaces": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\interfaces.js",
      "rxjs/add/operator/zipAll": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\zipAll.js",
      "rxjs/add/operator/zip": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\zip.js",
      "rxjs/add/operator/withLatestFrom": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\withLatestFrom.js",
      "rxjs/add/operator/windowWhen": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\windowWhen.js",
      "rxjs/add/operator/windowToggle": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\windowToggle.js",
      "rxjs/add/operator/windowTime": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\windowTime.js",
      "rxjs/add/operator/windowCount": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\windowCount.js",
      "rxjs/add/operator/window": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\window.js",
      "rxjs/add/operator/toPromise": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\toPromise.js",
      "rxjs/add/operator/toArray": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\toArray.js",
      "rxjs/add/operator/timestamp": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\timestamp.js",
      "rxjs/add/operator/timeoutWith": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\timeoutWith.js",
      "rxjs/add/operator/timeout": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\timeout.js",
      "rxjs/add/operator/timeInterval": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\timeInterval.js",
      "rxjs/add/operator/throttleTime": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\throttleTime.js",
      "rxjs/add/operator/throttle": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\throttle.js",
      "rxjs/add/operator/takeWhile": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\takeWhile.js",
      "rxjs/add/operator/takeUntil": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\takeUntil.js",
      "rxjs/add/operator/takeLast": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\takeLast.js",
      "rxjs/add/operator/take": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\take.js",
      "rxjs/add/operator/switchMapTo": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\switchMapTo.js",
      "rxjs/add/operator/switchMap": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\switchMap.js",
      "rxjs/add/operator/switch": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\switch.js",
      "rxjs/add/operator/subscribeOn": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\subscribeOn.js",
      "rxjs/add/operator/startWith": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\startWith.js",
      "rxjs/add/operator/skipWhile": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\skipWhile.js",
      "rxjs/add/operator/skipUntil": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\skipUntil.js",
      "rxjs/add/operator/skipLast": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\skipLast.js",
      "rxjs/add/operator/skip": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\skip.js",
      "rxjs/add/operator/single": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\single.js",
      "rxjs/add/operator/shareReplay": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\shareReplay.js",
      "rxjs/add/operator/share": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\share.js",
      "rxjs/add/operator/sequenceEqual": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\sequenceEqual.js",
      "rxjs/add/operator/scan": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\scan.js",
      "rxjs/add/operator/sampleTime": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\sampleTime.js",
      "rxjs/add/operator/sample": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\sample.js",
      "rxjs/add/operator/retryWhen": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\retryWhen.js",
      "rxjs/add/operator/retry": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\retry.js",
      "rxjs/add/operator/repeatWhen": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\repeatWhen.js",
      "rxjs/add/operator/repeat": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\repeat.js",
      "rxjs/add/operator/reduce": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\reduce.js",
      "rxjs/add/operator/race": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\race.js",
      "rxjs/add/operator/publishReplay": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\publishReplay.js",
      "rxjs/add/operator/publishLast": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\publishLast.js",
      "rxjs/add/operator/publishBehavior": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\publishBehavior.js",
      "rxjs/add/operator/publish": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\publish.js",
      "rxjs/add/operator/pluck": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\pluck.js",
      "rxjs/add/operator/partition": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\partition.js",
      "rxjs/add/operator/pairwise": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\pairwise.js",
      "rxjs/add/operator/onErrorResumeNext": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\onErrorResumeNext.js",
      "rxjs/add/operator/observeOn": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\observeOn.js",
      "rxjs/add/operator/multicast": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\multicast.js",
      "rxjs/add/operator/min": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\min.js",
      "rxjs/add/operator/mergeScan": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\mergeScan.js",
      "rxjs/add/operator/mergeMapTo": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\mergeMapTo.js",
      "rxjs/add/operator/mergeMap": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\mergeMap.js",
      "rxjs/add/operator/mergeAll": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\mergeAll.js",
      "rxjs/add/operator/merge": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\merge.js",
      "rxjs/add/operator/max": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\max.js",
      "rxjs/add/operator/materialize": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\materialize.js",
      "rxjs/add/operator/mapTo": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\mapTo.js",
      "rxjs/add/operator/map": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\map.js",
      "rxjs/add/operator/let": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\let.js",
      "rxjs/add/operator/last": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\last.js",
      "rxjs/add/operator/isEmpty": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\isEmpty.js",
      "rxjs/add/operator/ignoreElements": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\ignoreElements.js",
      "rxjs/add/operator/groupBy": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\groupBy.js",
      "rxjs/add/operator/first": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\first.js",
      "rxjs/add/operator/findIndex": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\findIndex.js",
      "rxjs/add/operator/find": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\find.js",
      "rxjs/add/operator/finally": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\finally.js",
      "rxjs/add/operator/filter": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\filter.js",
      "rxjs/add/operator/expand": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\expand.js",
      "rxjs/add/operator/exhaustMap": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\exhaustMap.js",
      "rxjs/add/operator/exhaust": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\exhaust.js",
      "rxjs/add/operator/every": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\every.js",
      "rxjs/add/operator/elementAt": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\elementAt.js",
      "rxjs/add/operator/do": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\do.js",
      "rxjs/add/operator/distinctUntilKeyChanged": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\distinctUntilKeyChanged.js",
      "rxjs/add/operator/distinctUntilChanged": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\distinctUntilChanged.js",
      "rxjs/add/operator/distinct": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\distinct.js",
      "rxjs/add/operator/dematerialize": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\dematerialize.js",
      "rxjs/add/operator/delayWhen": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\delayWhen.js",
      "rxjs/add/operator/delay": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\delay.js",
      "rxjs/add/operator/defaultIfEmpty": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\defaultIfEmpty.js",
      "rxjs/add/operator/debounceTime": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\debounceTime.js",
      "rxjs/add/operator/debounce": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\debounce.js",
      "rxjs/add/operator/count": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\count.js",
      "rxjs/add/operator/concatMapTo": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\concatMapTo.js",
      "rxjs/add/operator/concatMap": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\concatMap.js",
      "rxjs/add/operator/concatAll": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\concatAll.js",
      "rxjs/add/operator/concat": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\concat.js",
      "rxjs/add/operator/combineLatest": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\combineLatest.js",
      "rxjs/add/operator/combineAll": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\combineAll.js",
      "rxjs/add/operator/catch": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\catch.js",
      "rxjs/add/operator/bufferWhen": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\bufferWhen.js",
      "rxjs/add/operator/bufferToggle": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\bufferToggle.js",
      "rxjs/add/operator/bufferTime": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\bufferTime.js",
      "rxjs/add/operator/bufferCount": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\bufferCount.js",
      "rxjs/add/operator/buffer": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\buffer.js",
      "rxjs/add/operator/auditTime": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\auditTime.js",
      "rxjs/add/operator/audit": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\operator\\audit.js",
      "rxjs/add/observable/zip": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\zip.js",
      "rxjs/add/observable/using": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\using.js",
      "rxjs/add/observable/timer": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\timer.js",
      "rxjs/add/observable/throw": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\throw.js",
      "rxjs/add/observable/range": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\range.js",
      "rxjs/add/observable/race": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\race.js",
      "rxjs/add/observable/pairs": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\pairs.js",
      "rxjs/add/observable/onErrorResumeNext": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\onErrorResumeNext.js",
      "rxjs/add/observable/of": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\of.js",
      "rxjs/add/observable/never": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\never.js",
      "rxjs/add/observable/merge": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\merge.js",
      "rxjs/add/observable/interval": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\interval.js",
      "rxjs/add/observable/if": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\if.js",
      "rxjs/add/observable/generate": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\generate.js",
      "rxjs/add/observable/fromPromise": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\fromPromise.js",
      "rxjs/add/observable/fromEventPattern": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\fromEventPattern.js",
      "rxjs/add/observable/fromEvent": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\fromEvent.js",
      "rxjs/add/observable/from": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\from.js",
      "rxjs/add/observable/forkJoin": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\forkJoin.js",
      "rxjs/add/observable/empty": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\empty.js",
      "rxjs/add/observable/dom/webSocket": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\dom\\webSocket.js",
      "rxjs/add/observable/dom/ajax": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\dom\\ajax.js",
      "rxjs/add/observable/defer": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\defer.js",
      "rxjs/add/observable/concat": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\concat.js",
      "rxjs/add/observable/combineLatest": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\combineLatest.js",
      "rxjs/add/observable/bindNodeCallback": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\bindNodeCallback.js",
      "rxjs/add/observable/bindCallback": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\add\\observable\\bindCallback.js",
      "rxjs/Subscription": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\Subscription.js",
      "rxjs/Subscriber": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\Subscriber.js",
      "rxjs/SubjectSubscription": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\SubjectSubscription.js",
      "rxjs/Subject": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\Subject.js",
      "rxjs/Scheduler": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\Scheduler.js",
      "rxjs/Rx": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\Rx.js",
      "rxjs/ReplaySubject": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\ReplaySubject.js",
      "rxjs/OuterSubscriber": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\OuterSubscriber.js",
      "rxjs/Operator": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\Operator.js",
      "rxjs/Observer": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\Observer.js",
      "rxjs/Observable": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\Observable.js",
      "rxjs/Notification": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\Notification.js",
      "rxjs/InnerSubscriber": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\InnerSubscriber.js",
      "rxjs/BehaviorSubject": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\BehaviorSubject.js",
      "rxjs/AsyncSubject": "E:\\nastava\\2017-2018\\zimskiSemestar\\nwt\\2017\\Angular\\01_Uvod\\code\\primer1\\node_modules\\rxjs\\_esm5\\AsyncSubject.js"
    },
    "mainFields": [
      "browser",
      "module",
      "main"
    ]
  },
  "resolveLoader": {
    "modules": [
      "./node_modules",
      "./node_modules"
    ]
  },
  "entry": {
    "main": [
      "./src\\main.ts"
    ],
    "polyfills": [
      "./src\\polyfills.ts"
    ],
    "styles": [
      "./node_modules\\bootstrap\\dist\\css\\bootstrap.min.css",
      "./src\\styles.css"
    ]
  },
  "output": {
    "path": path.join(process.cwd(), "dist"),
    "filename": "[name].bundle.js",
    "chunkFilename": "[id].chunk.js",
    "crossOriginLoading": false
  },
  "module": {
    "rules": [
      {
        "test": /\.html$/,
        "loader": "raw-loader"
      },
      {
        "test": /\.(eot|svg|cur)$/,
        "loader": "file-loader",
        "options": {
          "name": "[name].[hash:20].[ext]",
          "limit": 10000
        }
      },
      {
        "test": /\.(jpg|png|webp|gif|otf|ttf|woff|woff2|ani)$/,
        "loader": "url-loader",
        "options": {
          "name": "[name].[hash:20].[ext]",
          "limit": 10000
        }
      },
      {
        "exclude": [
          path.join(process.cwd(), "node_modules\\bootstrap\\dist\\css\\bootstrap.min.css"),
          path.join(process.cwd(), "src\\styles.css")
        ],
        "test": /\.css$/,
        "use": [
          "exports-loader?module.exports.toString()",
          {
            "loader": "css-loader",
            "options": {
              "sourceMap": false,
              "importLoaders": 1
            }
          },
          {
            "loader": "postcss-loader",
            "options": {
              "ident": "postcss",
              "plugins": postcssPlugins
            }
          }
        ]
      },
      {
        "exclude": [
          path.join(process.cwd(), "node_modules\\bootstrap\\dist\\css\\bootstrap.min.css"),
          path.join(process.cwd(), "src\\styles.css")
        ],
        "test": /\.scss$|\.sass$/,
        "use": [
          "exports-loader?module.exports.toString()",
          {
            "loader": "css-loader",
            "options": {
              "sourceMap": false,
              "importLoaders": 1
            }
          },
          {
            "loader": "postcss-loader",
            "options": {
              "ident": "postcss",
              "plugins": postcssPlugins
            }
          },
          {
            "loader": "sass-loader",
            "options": {
              "sourceMap": false,
              "precision": 8,
              "includePaths": []
            }
          }
        ]
      },
      {
        "exclude": [
          path.join(process.cwd(), "node_modules\\bootstrap\\dist\\css\\bootstrap.min.css"),
          path.join(process.cwd(), "src\\styles.css")
        ],
        "test": /\.less$/,
        "use": [
          "exports-loader?module.exports.toString()",
          {
            "loader": "css-loader",
            "options": {
              "sourceMap": false,
              "importLoaders": 1
            }
          },
          {
            "loader": "postcss-loader",
            "options": {
              "ident": "postcss",
              "plugins": postcssPlugins
            }
          },
          {
            "loader": "less-loader",
            "options": {
              "sourceMap": false
            }
          }
        ]
      },
      {
        "exclude": [
          path.join(process.cwd(), "node_modules\\bootstrap\\dist\\css\\bootstrap.min.css"),
          path.join(process.cwd(), "src\\styles.css")
        ],
        "test": /\.styl$/,
        "use": [
          "exports-loader?module.exports.toString()",
          {
            "loader": "css-loader",
            "options": {
              "sourceMap": false,
              "importLoaders": 1
            }
          },
          {
            "loader": "postcss-loader",
            "options": {
              "ident": "postcss",
              "plugins": postcssPlugins
            }
          },
          {
            "loader": "stylus-loader",
            "options": {
              "sourceMap": false,
              "paths": []
            }
          }
        ]
      },
      {
        "include": [
          path.join(process.cwd(), "node_modules\\bootstrap\\dist\\css\\bootstrap.min.css"),
          path.join(process.cwd(), "src\\styles.css")
        ],
        "test": /\.css$/,
        "use": [
          "style-loader",
          {
            "loader": "css-loader",
            "options": {
              "sourceMap": false,
              "importLoaders": 1
            }
          },
          {
            "loader": "postcss-loader",
            "options": {
              "ident": "postcss",
              "plugins": postcssPlugins
            }
          }
        ]
      },
      {
        "include": [
          path.join(process.cwd(), "node_modules\\bootstrap\\dist\\css\\bootstrap.min.css"),
          path.join(process.cwd(), "src\\styles.css")
        ],
        "test": /\.scss$|\.sass$/,
        "use": [
          "style-loader",
          {
            "loader": "css-loader",
            "options": {
              "sourceMap": false,
              "importLoaders": 1
            }
          },
          {
            "loader": "postcss-loader",
            "options": {
              "ident": "postcss",
              "plugins": postcssPlugins
            }
          },
          {
            "loader": "sass-loader",
            "options": {
              "sourceMap": false,
              "precision": 8,
              "includePaths": []
            }
          }
        ]
      },
      {
        "include": [
          path.join(process.cwd(), "node_modules\\bootstrap\\dist\\css\\bootstrap.min.css"),
          path.join(process.cwd(), "src\\styles.css")
        ],
        "test": /\.less$/,
        "use": [
          "style-loader",
          {
            "loader": "css-loader",
            "options": {
              "sourceMap": false,
              "importLoaders": 1
            }
          },
          {
            "loader": "postcss-loader",
            "options": {
              "ident": "postcss",
              "plugins": postcssPlugins
            }
          },
          {
            "loader": "less-loader",
            "options": {
              "sourceMap": false
            }
          }
        ]
      },
      {
        "include": [
          path.join(process.cwd(), "node_modules\\bootstrap\\dist\\css\\bootstrap.min.css"),
          path.join(process.cwd(), "src\\styles.css")
        ],
        "test": /\.styl$/,
        "use": [
          "style-loader",
          {
            "loader": "css-loader",
            "options": {
              "sourceMap": false,
              "importLoaders": 1
            }
          },
          {
            "loader": "postcss-loader",
            "options": {
              "ident": "postcss",
              "plugins": postcssPlugins
            }
          },
          {
            "loader": "stylus-loader",
            "options": {
              "sourceMap": false,
              "paths": []
            }
          }
        ]
      },
      {
        "test": /\.ts$/,
        "loader": "@ngtools/webpack"
      }
    ]
  },
  "plugins": [
    new NoEmitOnErrorsPlugin(),
    new CopyWebpackPlugin([
      {
        "context": "src",
        "to": "",
        "from": {
          "glob": "assets/**/*",
          "dot": true
        }
      },
      {
        "context": "src",
        "to": "",
        "from": {
          "glob": "favicon.ico",
          "dot": true
        }
      }
    ], {
      "ignore": [
        ".gitkeep"
      ],
      "debug": "warning"
    }),
    new ProgressPlugin(),
    new CircularDependencyPlugin({
      "exclude": /(\\|\/)node_modules(\\|\/)/,
      "failOnError": false
    }),
    new NamedLazyChunksWebpackPlugin(),
    new HtmlWebpackPlugin({
      "template": "./src\\index.html",
      "filename": "./index.html",
      "hash": false,
      "inject": true,
      "compile": true,
      "favicon": false,
      "minify": false,
      "cache": true,
      "showErrors": true,
      "chunks": "all",
      "excludeChunks": [],
      "title": "Webpack App",
      "xhtml": true,
      "chunksSortMode": function sort(left, right) {
        let leftIndex = entryPoints.indexOf(left.names[0]);
        let rightindex = entryPoints.indexOf(right.names[0]);
        if (leftIndex > rightindex) {
            return 1;
        }
        else if (leftIndex < rightindex) {
            return -1;
        }
        else {
            return 0;
        }
    }
    }),
    new BaseHrefWebpackPlugin({}),
    new CommonsChunkPlugin({
      "name": [
        "inline"
      ],
      "minChunks": null
    }),
    new CommonsChunkPlugin({
      "name": [
        "vendor"
      ],
      "minChunks": (module) => {
                return module.resource
                    && (module.resource.startsWith(nodeModules)
                        || module.resource.startsWith(genDirNodeModules)
                        || module.resource.startsWith(realNodeModules));
            },
      "chunks": [
        "main"
      ]
    }),
    new SourceMapDevToolPlugin({
      "filename": "[file].map[query]",
      "moduleFilenameTemplate": "[resource-path]",
      "fallbackModuleFilenameTemplate": "[resource-path]?[hash]",
      "sourceRoot": "webpack:///"
    }),
    new CommonsChunkPlugin({
      "name": [
        "main"
      ],
      "minChunks": 2,
      "async": "common"
    }),
    new NamedModulesPlugin({}),
    new AngularCompilerPlugin({
      "mainPath": "main.ts",
      "platform": 0,
      "hostReplacementPaths": {
        "environments\\environment.ts": "environments\\environment.ts"
      },
      "sourceMap": true,
      "tsConfigPath": "src\\tsconfig.app.json",
      "skipCodeGeneration": true,
      "compilerOptions": {}
    })
  ],
  "node": {
    "fs": "empty",
    "global": true,
    "crypto": "empty",
    "tls": "empty",
    "net": "empty",
    "process": true,
    "module": false,
    "clearImmediate": false,
    "setImmediate": false
  },
  "devServer": {
    "historyApiFallback": true
  }
};

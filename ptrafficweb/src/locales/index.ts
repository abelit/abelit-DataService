import Vue from 'vue';
import VueI18n from 'vue-i18n';

// import element-ui translations
import elementEnLocale from 'element-ui/lib/locale/lang/en';
import elementZhLocale from 'element-ui/lib/locale/lang/zh-CN';

// import custom translations
import dsEnLocale from './en-US';
import dsZhLocale from './zh-CN';

Vue.use(VueI18n);

const messages = {
  // 或者用 Object.assign({ message: 'hello' }, dsEnLocale)
  en: {
    ...dsEnLocale,
    ...elementEnLocale
  },
  zh: {
    ...dsZhLocale,
    ...elementZhLocale
  }
};

// Create VueI18n instance with options
const i18n: VueI18n = new VueI18n({
  // set locale
  // options: en | zh
  locale: 'zh',
  // set locale messages
  messages
});

export default i18n;

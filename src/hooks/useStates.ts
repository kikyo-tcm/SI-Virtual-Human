import { ref } from 'vue'
import {AnimationsList} from '../store/vmdMapper'

export const Chars = [
  '八重神子',
  'Thoth',
  'Thoth2',
  'Bastet',
  'Hades',
  'Gengchen',
  'Yingzhao',
  'Yingzhao2',
  'Lingguang',
  'Sekhmet',
  'Jin-ei',
  'Hera',
  '桔梗',
  '娜塔莎'
]


export const Motions =  AnimationsList 
// ['Miku', 'Zyy', 'Stand', 'iKun1', 'iKun2', 'Run','waving happily','so happy','Blowing Kiss']

export const FPS = ref(0)
export const SelectedChar = ref('八重神子')
export const SelectedAnimation = ref('Stand')
export const PhysicsEnabled = ref(true)
export const ShowRigidBodies = ref(false)
export const ShowFPS = ref(true)
export const OpenAI_API_KEY = ref('')

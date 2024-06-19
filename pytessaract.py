
from PIL import Image
import pytesseract
medical_union_keywords = [
    'نقابة', 'الأطباء', 'بطاقة', 'عضوية', 'طبية', 'البشري', 'الدكتور', 'دكتور', 'الطبية',
    'طبي', 'مستشفى', 'علاج', 'صحة', 'العناية', 'الطبيب', 'الطب', 'ممارس', 'ممارسة', 'مجلس', 'الصحية'
]

def words_found_in_text(text, words):
    for word in words:
        if word in text:
            return True
    return False

def ocr(image_path):
    try:
        image = Image.open(image_path)
    except Exception as e:
        return {'error': f'Invalid image file: {str(e)}'}
    
    try:
        text = pytesseract.image_to_string(image, lang='ara')
    except Exception as e:
        return {'error': f'OCR processing failed: {str(e)}'}
    
    is_medical_union_card = words_found_in_text(text, medical_union_keywords)
    return {'is_medical_union_card': is_medical_union_card}

if __name__ == '__main__':
    image_path = 'download.jpg' 
    result = ocr(image_path)
    print(result)

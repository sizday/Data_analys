import nltk
import string
from nltk.corpus import stopwords
import pymorphy2
import matplotlib.pyplot as plt


def tokenize_me(file_text):
    stop_symbol = string.punctuation + '…«»0123456789qwerrtyuioplkjhgfdsazxcvbnmQWERTYUIOKLPJHGFDSAZXCVBNM￼₽󾓬'
    stop_list = ['россияхорватия', 'росс', 'ссия', 'грать', 'рить', 'дить', 'сбор', 'сбор', 'весь']
    line_clear = [i for i in file_text if (i not in stop_symbol)]
    file_text = ""
    for i in range(len(line_clear)):
        file_text += line_clear[i]
    token = nltk.word_tokenize(file_text)
    token = [morph.parse(i)[0].normal_form for i in token]
    stop_words = stopwords.words('russian')
    token = [i for i in token if ((i not in stop_words) & (i not in stop_list) & (len(i) > 3) & (len(i) < 12))]
    return token


def list_twitter(file_text):
    list_twit = file_text.split('\n')
    list_twit = [i for i in list_twit if (i != '')]
    token = []
    for i in range(len(list_twit)):
        twit = ''
        token_twit = tokenize_me(list_twit[i])
        for j in range(len(token_twit)):
            twit = twit + token_twit[j] + ' '
            token.append(token_twit[j])
        list_twit[i] = twit
    tokens_one = list(set(token))
    """
    open('1.txt', 'w').close()
    f1 = open('1.txt', 'a', encoding='utf-8')
    for i in range(len(list_twit)):
        f1.write(list_twit[i] + '\n')
    open('2.txt', 'w').close()
    f2 = open('2.txt', 'a', encoding='utf-8')
    for i in range(len(tokens_one)):
        f2.write(tokens_one[i] + '\n')
    """
    return tokens_one, list_twit


def frequency(token, twit):
    number = []
    for i in range(len(token)):
        k = 0
        for j in range(len(twit)):
            if twit[j].find(token[i]) != -1:
                k += 1
        number.append(k)
    fr = []
    for i in range(len(token)):
        fr.append([token[i], str(number[i])])
    fr = sorted(fr, key=lambda x: int(x[1]), reverse=True)
    return fr


def adjectives(document):
    f7 = open('estimations.txt', encoding="utf-8")
    open('adjectives.txt', 'w', encoding='utf-8').close()
    f8 = open('adjectives.txt', 'a', encoding='utf-8')
    s = f7.read()
    list_word = s.split('\n')
    coeff = []
    k1 = k2 = 0
    pos = ['', '', '']
    neg = ['', '', '']
    pos_n = [0, 0, 0]
    neg_n = [0, 0, 0]
    for i in range(len(list_word)):
        c = list_word[i].split(' ')
        coeff.append(c[1])
    f8.write("Top-3 positive:\n")
    for i in range(len(document)):
        if (k1 < 3) & (coeff[i] == '1'):
            p = morph.parse(document[i][0])[0]
            tags = p.tag.POS
            if tags == 'ADJF':
                f8.write('{} - {} - {}%\n'.format(document[i][0], document[i][1], float(document[i][1]) / 100))
                pos[k1] = document[i][0]
                pos_n[k1] = int(document[i][1])
                k1 += 1
    f8.write("\nTop-3 negative:\n")
    for i in range(len(document)):
        if (k2 < 3) & (coeff[i] == '-1'):
            p = morph.parse(document[i][0])[0]
            tags = p.tag.POS
            if tags == 'ADJF':
                f8.write('{} - {} - {}%\n'.format(document[i][0], document[i][1], float(document[i][1]) / 100))
                neg[k2] = document[i][0]
                neg_n[k2] = int(document[i][1])
                k2 += 1
    f7.close()
    f8.close()
    bar_chart(pos_n[2], pos_n[1], pos_n[0], 'Top-3 Positive', (pos[0], pos[1], pos[2]), 2, 1, 1)
    bar_chart(neg_n[2], neg_n[1], neg_n[0], 'Top-3 Negative', (neg[0], neg[1], neg[2]), 2, 1, 2)
    plt.savefig(r'D:\bar1.png')
    plt.show()


def time_rules(twit):
    t_low = -1
    t_up = 1
    f = open('data.txt', encoding="utf-8")
    s = f.read()
    list_twit = s.split('\n')
    list_twit = [i for i in list_twit if (i != '')]
    stack_time = [0]
    for i in range(1, len(list_twit)):
        stack_time.append(100)
        date = list_twit[i][:10]
        time = list_twit[i][11:16]
        hour = int(time[:2])
        minute = int(time[3:5])
        minute = hour * 60 + minute
        j = 0
        if date == '2018-07-08':
            if minute < 30:
                stack_time[i] = 0
            else:
                while minute < 240 - 10*j:
                    stack_time[i] = 21 - j
                    j += 1
    f5 = open('estimations.txt', encoding='utf-8')
    s = f5.read()
    list_word = s.split('\n')
    list_mark = []
    for i in range(len(list_word)):
        sp = list_word[i].split(' ')
        list_word[i] = sp[0]
        list_mark.append(int(sp[1]))
    twit = [i for i in twit if (i != '')]
    stack1_pos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    stack1_neg = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    stack1_net = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(twit)):
            sum = 0
            twit_word = twit[i].split(' ')
            for j in range(len(twit_word)-1):
                num = list_word.index(twit_word[j])
                sum += list_mark[num]
            for k in range(22):
                if stack_time[i] <= k:
                    if sum > t_up:
                        stack1_pos[k] += 1
                    elif sum < t_low:
                        stack1_neg[k] += 1
                    else:
                        stack1_net[k] += 1
    open('hours.txt', 'w', encoding='utf-8').close()
    f9 = open('hours.txt', 'a', encoding='utf-8')
    time_start = ['00:00', '00:30', '00:40', '00:50', '01:00', '01:00', '01:10', '01:20', '01:30', '01:40', '01:50',
                  '02:00', '02:10', '02:20', '02:30', '02:40', '02:50', '03:00', '03:10', '03:20', '03:30', '03:40', '03:50']
    time_end = ['00:30', '00:40', '00:50', '01:00', '01:00', '01:10', '01:20', '01:30', '01:40', '01:50', '02:00',
                '02:10', '02:20', '02:30', '02:40', '02:50', '03:00', '03:10', '03:20', '03:30', '03:40', '03:50', '04:00']
    for k in range(22):
        count_twit = stack1_pos[k] + stack1_neg[k] + stack1_net[k]
        stack1_pos[k] = round(stack1_pos[k] / count_twit, 3)
        stack1_neg[k] = round(stack1_neg[k] / count_twit, 3)
        stack1_net[k] = round(stack1_net[k] / count_twit, 3)
        if k == 0:
            start = 0
        else:
            start = 30 + 10 * (k-1)
        end = 30 + 10 * k
        start_h = str(int(start / 60))
        start_m = str(start % 60)
        end_h = str(int(end / 60))
        end_m = str(end % 60)
        if start_m == '0':
            start_m = '00'
        if end_m == '0':
            end_m = '00'
        f9.write('0{}:{} - 0{}:{} : {} {}/{}/{}\n'.format(start_h, start_m, end_h, end_m, count_twit,
                                                          stack1_pos[k], stack1_net[k], stack1_neg[k]))
        plt.subplot(2, 1, 1)
        plt.ylabel('Fraction')
        plt.scatter(time_end[k], stack1_pos[k], c='green')
        plt.scatter(time_end[k], stack1_net[k], c='yellow')
        plt.scatter(time_end[k], stack1_neg[k], c='red')
        if k != 0:
            xm = [time_end[k], time_end[k-1]]
            ym = [stack1_pos[k], stack1_pos[k-1]]
            plt.plot(xm, ym, c='green')
            xm = [time_end[k], time_end[k - 1]]
            ym = [stack1_net[k], stack1_net[k - 1]]
            plt.plot(xm, ym, c='yellow')
            xm = [time_end[k], time_end[k - 1]]
            ym = [stack1_neg[k], stack1_neg[k - 1]]
            plt.plot(xm, ym, c='red')
        plt.subplot(2, 1, 2)
        plt.ylabel('Number of tweets')
        plt.title('Time window')
        plt.scatter(time_end[k], count_twit, c='black')
        xm = [time_end[k], time_end[k]]
        ym = [0, count_twit]
        plt.plot(xm, ym, c='black')
    plt.savefig(r'D:\bar3.png')
    plt.show()


def rules(twit):
    t_low = -1
    t_up = 1
    count1_pos = count1_neg = count1_net = count2_pos = count2_neg = count2_net = 0
    count3_pos = count3_neg = count3_net = count4_pos = count4_neg = count4_net = 0
    f5 = open('estimations.txt', encoding='utf-8')
    s = f5.read()
    list_word = s.split('\n')
    list_mark = []
    for i in range(len(list_word)):
        sp = list_word[i].split(' ')
        list_word[i] = sp[0]
        list_mark.append(int(sp[1]))
    twit = [i for i in twit if (i != '')]
    for i in range(len(twit)):
        sum = 0
        twit_word = twit[i].split(' ')
        count2_pos_cur = 0
        count2_neg_cur = 0
        count2_net_cur = 0
        count4_pos_cur = True
        count4_neg_cur = True
        for j in range(len(twit_word)-1):
            num = list_word.index(twit_word[j])
            sum += list_mark[num]
            if list_mark[num] == 1:
                count2_pos_cur += 1
            elif list_mark[num] == -1:
                count2_neg_cur += 1
            else:
                count2_net_cur += 1
            if (j <= 2) & (j >= 0):
                if list_mark[num] != 1:
                    count4_pos_cur = False
                elif list_mark[num] != -1:
                    count4_neg_cur = False
        if max(count2_pos_cur, count2_neg_cur, count2_net_cur) == count2_pos_cur:
            count2_pos += 1
        elif max(count2_pos_cur, count2_neg_cur, count2_net_cur) == count2_neg_cur:
            count2_neg += 1
        else:
            count2_net += 1
        if (count2_pos_cur - count2_neg_cur) > 0.5 * (count2_pos_cur + count2_neg_cur + count2_net_cur):
            count3_pos += 1
        elif (count2_neg_cur - count2_pos_cur) > 0.5 * (count2_pos_cur + count2_neg_cur + count2_net_cur):
            count3_neg += 1
        else:
            count3_net += 1
        if sum > t_up:
            count1_pos += 1
        elif sum < t_low:
            count1_neg += 1
        else:
            count1_net += 1
        if count4_pos_cur:
            count4_pos += 1
        elif count4_neg_cur:
            count4_neg += 1
        else:
            count4_net += 1
    open('classifications.txt', 'w', encoding='utf-8').close()
    f6 = open('classifications.txt', 'a', encoding='utf-8')
    amount = count1_pos + count1_neg + count1_net
    f6.write('Sum of marks\nGood - {} - {}%\nBad - {} - {}%\n'
             'Neutral - {} - {}%\n\n'.format(count1_pos, float(count1_pos) / amount * 100, count1_neg,
                                        float(count1_neg) / amount * 100, count1_net, float(count1_net) / amount * 100))
    f6.write('Max part\nGood - {} - {}%\nBad - {} - {}%\n'
             'Neutral - {} - {}%\n\n'.format(count2_pos, float(count2_pos) / amount * 100, count2_neg,
                                        float(count2_neg) / amount * 100, count2_net, float(count2_net) / amount * 100))
    f6.write('The difference in percentage\nGood - {} - {}%\nBad - {} - {}%\n'
             'Neutral - {} - {}%\n\n'.format(count3_pos, float(count3_pos) / amount * 100, count3_neg,
                                        float(count3_neg) / amount * 100, count3_net, float(count3_net) / amount * 100))
    f6.write('3 in a row\nGood - {} - {}%\nBad - {} - {}%\n'
             'Neutral - {} - {}%\n\n'.format(count4_pos, float(count4_pos) / amount * 100, count4_neg,
                                        float(count4_neg) / amount * 100, count4_net, float(count4_net) / amount * 100))
    bar_chart(count1_pos, count1_neg, count1_net, 'Sum of marks', ('Positive', 'Negative', 'Neutral'), 2, 2, 1)
    bar_chart(count2_pos, count2_neg, count2_net, 'Max part', ('Positive', 'Negative', 'Neutral'), 2, 2, 2)
    bar_chart(count3_pos, count3_neg, count3_net, 'The difference in percentage', ('Positive', 'Negative', 'Neutral'), 2, 2, 3)
    bar_chart(count4_pos, count4_neg, count4_net, '3 in a row', ('Positive', 'Negative', 'Neutral'), 2, 2, 4)
    plt.savefig(r'D:\bar2.png')
    plt.show()
    f5.close()
    f6.close()


def bar_chart(x, y, z, name_rule, objects, n1, n2, n3):
    plt.subplot(n1, n2, n3)
    y_pos = [0, 1, 2]
    performance = [x, y, z]
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Twits')
    plt.title(name_rule)


def main():
    f = open('data.txt', encoding="utf-8")
    s = f.read()
    after_changes = list_twitter(s)
    tokens = after_changes[0]
    twits = after_changes[1]
    # print(tokens)
    print(len(tokens))
    f.close()
    time_rules(twits)
    rules(twits)
    open('frequency.txt', 'w').close()
    freq = frequency(tokens, twits)
    f3 = open('frequency.txt', 'a', encoding='utf-8')
    for i in range(len(freq)):
        f3.write('{} - {} - {}%\n'.format(freq[i][0], freq[i][1], float(freq[i][1])/100))
    f3.close()
    adjectives(freq)


stop_list = ['россияхорватия', 'росс', 'ссия', 'грать', 'рить', 'дить', 'сбор', 'сбор', 'весь']
morph = pymorphy2.MorphAnalyzer()
main()

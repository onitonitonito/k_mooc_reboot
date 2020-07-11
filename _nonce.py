"""
* nonce 만이 유일하게 변경할 수 있는 값이다. 값을 1씩 증가 시키며 찾는다.
* 우연히 해쉬값의 첫자리가 '0000'으로 시작하는 해쉬를 발견 했을 때,
* 작업 증명을 완성 한다. 작업증명(Proof of Work) 값은 nonce=7725 이다.
"""
import time

import pyprnt
from hashlib import sha256

# difficulty 를 '0000' 에서 0 을 하나씩 늘려 실행시간을 비교한다.
difficulty = '000000'

mining_uid = 'node_identifier_uid'
transactions = [
    {
        'sender': 'Alice',
        'recipient': 'Bob',
        'amount': 1000
    },
    {
        'sender': 'Scrouge',
        'recipient': 'Alice',
        'amount': 800
    },
    {
        'sender': 'coinbase_reward',
        'recipient': mining_uid,
        'amount': 200
    },
]


last_block = {
    'index': 12,
    'difficulty': difficulty,
    'nonce': 0,
    'hash_previous': '000005fa8482b821aff9b2ce6103f69e',
    'transaction': transactions,
}


def get_hash_w_nonce(last_block, nonce):
    """ 최근블럭에 논스를 대입하여 해쉬값을 리턴한다"""
    last_block['nonce'] = nonce
    hash = sha256(str(last_block).encode()).hexdigest()
    return hash

def add_header(last_block, block_hash):
    """ 블럭에 타임스탬프와 현재해쉬를 추가한다"""
    header = {
        'timestamp': time.time(),
        'hash_present': block_hash, }

    for _key, _val in header.items():
        last_block[_key] = _val

    return last_block

def proof_of_work(last_block):
    nonce = 0
    difficulty = last_block['difficulty']

    while True:
        hash = get_hash_w_nonce(last_block, nonce)

        if hash[:len(difficulty)] == difficulty:
            hash_present = hash[:32]
            add_header(last_block, hash_present)
            return last_block

        nonce += 1


if __name__ == '__main__':
    last_block = proof_of_work(last_block)
    pyprnt.prnt(last_block)

from argparse import PARSER
import re



from Seqbio.calculation.SeqCal import gcContent, countBases
from Seqbio.pattern.SeqPattern import cpgSearch, enzTargetsScan
from Seqbio.seqMan.dnaconvert import transcription, reverseComplementSeq, translation

def asgparserlocal():
    from argparse import ArgumentParser
    parser = ArgumentParser(prog='myseq', description='Work with sequence')
    
    subparsers = parser.add_subparsers(
        title='commands',description='Please choose command below:', 
        dest='command'
    )
    subparsers.required = True

    cgc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    cgc_command.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
       
    
    cbase_command = subparsers.add_parser('countBases', help='Count number of each base')
    cbase_command.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    cbase_command.add_argument("-r", "--revcomp", action='store_true', default=False, help="Convet DNA to reverse-complementary")


    transcrip_command = subparsers.add_parser('transcription', help='Convert DNA->RNA')
    transcrip_command.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    transcrip_command.add_argument("-r", "--revcomp", action='store_true', default=False, help="Convet DNA to reverse-complementary")


    transla_command = subparsers.add_parser('translation', help='Convert DNA->Protein')
    transla_command.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    transla_command.add_argument("-r", "--revcomp", action='store_true', default=False,  help="Convet DNA to reverse-complementary")


    enzScan_command = subparsers.add_parser('enzTargetsScan', help='Find restriction enzyme')
    enzScan_command.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    enzScan_command.add_argument("-e","--enz", type=str, default=None, help="Enzyme name")
    enzScan_command.add_argument("-r", "--revcomp", action='store_true', default=False, help="Convet DNA to reverse-complementary")
    return parser


def main():
    
    parser = asgparserlocal()
    args = parser.parse_args()
    if args.command == 'gcContent':
        if args.seq == None:
            print("----\nError: Invalid input\n--------\n")
            exit(parser.parse_args(['gcContent','-h']))
        print('Input',args.seq, '\nGC content =',gcContent(args.seq))
        
    
    elif args.command == 'countBases':
        if not args.seq == None and not args.revcomp:
            print('Input',args.seq, '\ncountBases =', countBases(args.seq)) 
        elif not args.seq == None and args.revcomp:
            print('Input',args.seq, '\ncountBases =', countBases(reverseComplementSeq(args.seq)) )
        else:
            print("--------------\nError: Invalid input\n--------------------\n")
            exit(parser.parse_args(['countBases','-h']))
        

    elif args.command == 'transcription':
        if not args.seq == None and not args.revcomp:
            print('Input',args.seq, '\ntranscription =', transcription(args.seq))
        elif not args.seq == None and args.revcomp:
            print('Input',args.seq, '\ntranscription =', transcription(reverseComplementSeq(args.seq)) )
        else:
            print("--------------\nError: Invalid input\n--------------------\n")
            exit(parser.parse_args(['transcription','-h']))  


    elif args.command == 'translation':
        if not args.seq == None and not args.revcomp:
            print('Input',args.seq, '\ntranslation =', translation(args.seq)) 
        elif not args.seq == None and args.revcomp:
            print('Input',args.seq, '\ntranslation =', translation(reverseComplementSeq(args.seq)) )
        else:
            print("---------------\nError: Invalid input\n-------------------\n")
            exit(parser.parse_args(['translation','-h']))
                
        
    elif args.command == 'enzTargetsScan':
        if args.seq == None or args.enz == None:
            print("----------------\nError: Invalid input\n------------------\n")
            exit(parser.parse_args(['enzTargetsScan','-h']))
        elif not args.revcomp:
            print(args.enz, 'sites=', enzTargetsScan(args.seq, args.enz) )
        else: 
            print(args.enz, 'sites=', enzTargetsScan(reverseComplementSeq(args.seq), args.enz) )

  

  
    
if __name__ == '__main__':
    main()